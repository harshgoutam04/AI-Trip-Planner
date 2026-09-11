from langgraph.graph import StateGraph, END

from agent.state import TripState
from agent.nodes import validate_trip
from agent.tools import run_trip_planner


def router(state: TripState):
    """
    Decide what node to execute next.
    """

    if state["next_step"] == "ask_user":
        return "ask_user"

    return "plan_trip"


def ask_user(state: TripState):
    """
    Placeholder node.
    Later this will ask follow-up questions in Streamlit.
    """

    missing = state.get("missing", [])

    state["itinerary"] = (
        "I still need the following information:\n\n"
        + "\n".join(f"- {item}" for item in missing)
    )

    return state


workflow = StateGraph(TripState)

workflow.add_node(
    "validate_trip",
    validate_trip,
)

workflow.add_node(
    "ask_user",
    ask_user,
)

workflow.add_node(
    "plan_trip",
    run_trip_planner,
)

workflow.set_entry_point("validate_trip")

workflow.add_conditional_edges(
    "validate_trip",
    router,
    {
        "ask_user": "ask_user",
        "plan_trip": "plan_trip",
    },
)

workflow.add_edge("ask_user", END)
workflow.add_edge("plan_trip", END)

trip_graph = workflow.compile()