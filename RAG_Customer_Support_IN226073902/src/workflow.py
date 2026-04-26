from langgraph.graph import StateGraph, END
from typing import TypedDict
from rag_pipeline import generate_answer
from routing import decide_route
from hitl import human_intervention


# ✅ Define proper state schema
class State(TypedDict):
    query: str
    retriever: object
    answer: str
    route: str


def process_node(state: State):
    query = state.get("query")
    retriever = state.get("retriever")

    if not query:
        raise ValueError("Query missing in state")

    answer = generate_answer(retriever, query)

    state["answer"] = answer
    state["route"] = decide_route(answer)

    return state


def hitl_node(state: State):
    human_answer = human_intervention()
    state["answer"] = human_answer
    return state


def output_node(state: State):
    return state


def build_graph():
    graph = StateGraph(State)

    graph.add_node("process", process_node)
    graph.add_node("hitl", hitl_node)
    graph.add_node("output", output_node)

    graph.set_entry_point("process")

    graph.add_conditional_edges(
        "process",
        lambda state: state["route"],
        {
            "HITL": "hitl",
            "OUTPUT": "output"
        }
    )

    graph.add_edge("hitl", "output")
    graph.add_edge("output", END)

    return graph.compile()