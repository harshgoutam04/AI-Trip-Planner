def decide_next_step(state: dict):
    """
    Decide whether we have enough information
    to generate the travel plan.
    """

    planner = state["planner"]

    if planner.is_complete():

        return "complete"

    return "follow_up"