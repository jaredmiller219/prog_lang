#######################################
# NODES
#######################################

class NumberNode:
  def __init__(self, token):
    self.token = token
    self.position_start = self.token.position_start
    self.position_end = self.token.position_end

  def __repr__(self):
    return f'{self.token}'

class StringNode:
  def __init__(self, token):
    self.token = token
    self.position_start = self.token.position_start
    self.position_end = self.token.position_end

  def __repr__(self):
    return f'{self.token}'

class ListNode:
  def __init__(self, element_nodes, position_start, position_end):
    self.element_nodes = element_nodes
    self.position_start = position_start
    self.position_end = position_end


class VarAccessNode:
  def __init__(self, variable_name_token):
    self.variable_name_token = variable_name_token
    self.position_start = self.variable_name_token.position_start
    self.position_end = self.variable_name_token.position_end

class VarAssignNode:
  def __init__(self, variable_name_token, value_node):
    self.variable_name_token = variable_name_token
    self.value_node = value_node
    self.position_start = self.variable_name_token.position_start
    self.position_end = self.value_node.position_end

class BinaryOperationNode:
  def __init__(self, left_node, operation_token, right_node):
    self.left_node = left_node
    self.operation_token = operation_token
    self.right_node = right_node
    self.position_start = self.left_node.position_start
    self.position_end = self.right_node.position_end

  def __repr__(self):
    return f'({self.left_node}, {self.operation_token}, {self.right_node})'

class UnaryOpNode:
  def __init__(self, operation_token, node):
    self.operation_token = operation_token
    self.node = node
    self.position_start = self.operation_token.position_start
    self.position_end = node.position_end

  def __repr__(self):
    return f'({self.operation_token}, {self.node})'

class IfNode:
  def __init__(self, cases, else_case):
    self.cases = cases
    self.else_case = else_case
    self.position_start = self.cases[0][0].position_start
    self.position_end = (self.else_case or self.cases[len(self.cases) - 1])[0].position_end

class ForNode:
  def __init__(self, variable_name_token, start_value_node, end_value_node, step_value_node, body_node, should_return_null):
    self.variable_name_token = variable_name_token
    self.start_value_node = start_value_node
    self.end_value_node = end_value_node
    self.step_value_node = step_value_node
    self.body_node = body_node
    self.should_return_null = should_return_null
    self.position_start = self.variable_name_token.position_start
    self.position_end = self.body_node.position_end

class WhileNode:
  def __init__(self, condition_node, body_node, should_return_null):
    self.condition_node = condition_node
    self.body_node = body_node
    self.should_return_null = should_return_null
    self.position_start = self.condition_node.position_start
    self.position_end = self.body_node.position_end

class FuncDefNode:
  def __init__(self, variable_name_token, argument_name_tokens, body_node, should_auto_return):
    self.variable_name_token = variable_name_token
    self.argument_name_tokens = argument_name_tokens
    self.body_node = body_node
    self.should_auto_return = should_auto_return

    if self.variable_name_token:
      self.position_start = self.variable_name_token.position_start
    elif len(self.argument_name_tokens) > 0:
      self.position_start = self.argument_name_tokens[0].position_start
    else:
      self.position_start = self.body_node.position_start

    self.position_end = self.body_node.position_end

class CallNode:
  def __init__(self, node_to_call, argument_nodes):
    self.node_to_call = node_to_call
    self.argument_nodes = argument_nodes
    self.position_start = self.node_to_call.position_start

    if len(self.argument_nodes) > 0:
      self.position_end = self.argument_nodes[len(self.argument_nodes) - 1].position_end
    else:
      self.position_end = self.node_to_call.position_end

class ReturnNode:
  def __init__(self, node_to_return, position_start, position_end):
    self.node_to_return = node_to_return
    self.position_start = position_start
    self.position_end = position_end

class ContinueNode:
  def __init__(self, position_start, position_end):
    self.position_start = position_start
    self.position_end = position_end

class BreakNode:
  def __init__(self, position_start, position_end):
    self.position_start = position_start
    self.position_end = position_end
