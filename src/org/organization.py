from typing import Dict, Any
from langgraph.graph import StateGraph, END
import yaml
import networkx as nx
import matplotlib.pyplot as plt  # สำหรับ visualize (optional)

class OrgState:
    def __init__(self):
        self.current_agent = "CEO"
        self.task = ""
        self.results = {}
        self.context = {}

class ClawTeam:
    def __init__(self, config_path="config.yaml"):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        self.agents = self._build_agents()
        self.graph = self._build_graph()

    def _build_agents(self):
        # Placeholder: ในจริงจะ load จาก ClawTeam หรือ create dynamic
        agents = {}
        # ตัวอย่าง
        agents["CEO"] = {"role": self.config["organization"]["ceo"]["role"]}
        # ... เพิ่ม CFO, CTO ฯลฯ ตาม config
        return agents

    def _build_graph(self):
        graph = StateGraph(OrgState)
        
        def ceo_node(state: OrgState):
            # CEO decide delegate to which dept
            if "finance" in state.task.lower():
                state.current_agent = "CFO"
            elif "tech" in state.task.lower() or "security" in state.task.lower():
                state.current_agent = "CTO"
            # ... logic อื่น
            return state

        def dept_node(state: OrgState):
            # Dept head delegate ลง sub
            # ใช้ config เพื่อหา sub-agents
            return state

        graph.add_node("CEO", ceo_node)
        graph.add_node("Department", dept_node)
        # เพิ่ม node สำหรับแต่ละ level ตามต้องการ

        graph.set_entry_point("CEO")
        graph.add_edge("CEO", "Department")
        graph.add_edge("Department", END)  # หรือ loop ต่อ
        return graph.compile()

    def run_task(self, task: str):
        initial = OrgState()
        initial.task = task
        result = self.graph.invoke(initial)
        return result.results

    def visualize_org(self):
        G = nx.DiGraph()
        # Build graph จาก config.yaml
        G.add_edge("CEO", "CFO")
        G.add_edge("CEO", "CTO")
        G.add_edge("CEO", "COO")
        G.add_edge("CEO", "GC")
        # ... เพิ่มตาม flowchart
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue')
        plt.show()  # หรือ save fig
