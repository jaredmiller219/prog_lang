"use strict";
var __createBinding =
  (this && this.__createBinding) ||
  (Object.create
    ? function (o, m, k, k2) {
        if (k2 === undefined) k2 = k;
        var desc = Object.getOwnPropertyDescriptor(m, k);
        if (
          !desc ||
          ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)
        ) {
          desc = {
            enumerable: true,
            get: function () {
              return m[k];
            },
          };
        }
        Object.defineProperty(o, k2, desc);
      }
    : function (o, m, k, k2) {
        if (k2 === undefined) k2 = k;
        o[k2] = m[k];
      });
var __setModuleDefault =
  (this && this.__setModuleDefault) ||
  (Object.create
    ? function (o, v) {
        Object.defineProperty(o, "default", { enumerable: true, value: v });
      }
    : function (o, v) {
        o["default"] = v;
      });
var __importStar =
  (this && this.__importStar) ||
  (function () {
    var ownKeys = function (o) {
      ownKeys =
        Object.getOwnPropertyNames ||
        function (o) {
          var ar = [];
          for (var k in o)
            if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
          return ar;
        };
      return ownKeys(o);
    };
    return function (mod) {
      if (mod && mod.__esModule) return mod;
      var result = {};
      if (mod != null)
        for (var k = ownKeys(mod), i = 0; i < k.length; i++)
          if (k[i] !== "default") __createBinding(result, mod, k[i]);
      __setModuleDefault(result, mod);
      return result;
    };
  })();
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = activate;
exports.deactivate = deactivate;
const vscode = __importStar(require("vscode"));
const child_process_1 = require("child_process");
let outputChannel;
function activate(context) {
  outputChannel = vscode.window.createOutputChannel("JCode Output");
  let disposable = vscode.commands.registerCommand(
    "code-runner.run",
    async () => {
      const editor = vscode.window.activeTextEditor;
      if (
        !editor ||
        editor.document.isUntitled ||
        editor.document.uri.scheme !== "file" ||
        !editor.document.fileName.endsWith(".jcode")
      ) {
        vscode.window.showErrorMessage(
          "No active .jcode file - open a jcode (.jcode) file to run"
        );
        return;
      }
      const filePath = editor.document.uri.fsPath;
      const interpreterPath =
        vscode.workspace
          .getConfiguration("jcodeRunner")
          .get("interpreterPath") || "";
      if (!interpreterPath) {
        vscode.window.showErrorMessage(
          "Interpreter path not set. Please configure 'jcodeRunner.interpreterPath' in your settings."
        );
        return;
      }
      outputChannel.clear();
      outputChannel.show(true);
      (0, child_process_1.exec)(
        `python3 "${interpreterPath}" "${filePath}"`,
        (error, stdout, stderr) => {
          if (error) {
            outputChannel.appendLine(`Error: ${error.message}`);
          }
          if (stderr) {
            outputChannel.appendLine(`Stderr: ${stderr}`);
          }
          if (stdout) {
            outputChannel.appendLine(stdout);
          }
        }
      );
    }
  );
  context.subscriptions.push(disposable);
}
function deactivate() {
  outputChannel?.dispose();
}
//# sourceMappingURL=extension.js.map
