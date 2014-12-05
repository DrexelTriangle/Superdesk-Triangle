

states = []
actions = []
allowed_workflow_states = []

__all__ = ['workflow_state', 'get_workflow_states', 'allowed_workflow_states',
           'workflow_action', 'get_workflow_actions']


def workflow_action(name, include_states=None, exclude_states=None, privileges=None):
    """Register new workflow action.

    :param name: unique name of action
    :param include_states: include action if item state is in include_states
    :param exclude_states: exclude action if item state is in exclude_statese
    :param privileges: list of privileges required for this action
    """
    if include_states is None:
        include_states = []
    if exclude_states is None:
        exclude_states = []
    if privileges is None:
        privileges = []
    actions.append({
        'name': name,
        'exclude_states': exclude_states,
        'include_states': include_states,
        'privileges': privileges
    })


def get_workflow_actions(state=None):
    """Get list of all registered workflow actions.

    :param state: filter actions by given item state if provided
    """
    if state is None:
        return actions
    else:
        def is_go(action, state):
            if action['include_states']:
                return state in action['include_states']
            elif action['exclude_states']:
                return state not in action['exclude_states']
        return [action for action in actions if is_go(action, state)]


def workflow_state(name):
    """Register new workflow state.

    :param name: unique name of state
    """
    allowed_workflow_states.append(name)
    states.append({'name': name})


def get_workflow_states():
    """Get list of all registered workflow states."""
    return states
