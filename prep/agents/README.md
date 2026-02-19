# 10-Day Anthropic Agent Prep Plan

Build up from SDK fundamentals to a full agent system in 10 days, ~2 hours per day.
Designed for a 45-minute Colab-based agent build interview.

## Schedule Overview

| Day | Topic | Type | Key Deliverable |
|-----|-------|------|-----------------|
| 1 | SDK Fundamentals & Messages API | Learn + Build | Multi-turn chatbot with system prompts |
| 2 | Tool Use Basics | Learn + Build | Calculator agent with 3 tools |
| 3 | The Agent Loop | Core Build | Complete agent loop from scratch (THE interview pattern) |
| 4 | Error Handling & Structured Output | Build | Production-grade agent with error handling |
| 5 | ReAct Agent from Scratch | Build | ReAct agent with injected LLM + async variant |
| 6 | Streaming & Extended Thinking | Learn + Build | Streaming agent with extended thinking |
| 7 | MCP (Model Context Protocol) | Learn + Build | MCP server (hello-world + SQLite) |
| 8 | Workflow Patterns (Chains, Routing, Parallel) | Build | Three orchestration patterns |
| 9 | Full Agent System | Build | Multi-tool research agent end-to-end |
| 10 | Timed Practice & Review | Drill | 45-min timed build (interview sim) |

## Philosophy

From Anthropic's "Building Effective Agents" blog:
1. **Start simple.** Don't build an agent when a single LLM call works.
2. **Workflows before agents.** Fixed orchestration > autonomous loops.
3. **Agents are the last resort.** Only when task requires dynamic decisions.
4. **Invest in tool design.** Descriptions are an "agent-computer interface."
5. **Transparency.** Show planning steps.

## Reference Materials
- `../anthropic/api_primer.md` - Concise API primer (messages, tool use, streaming, thinking)
- `../anthropic/links.md` - URLs to all official docs
- `../anthropic/llms-full.txt` - Full Anthropic documentation (searchable)
- `../anthropic_agents.md` - Quick-reference cheat sheet for the interview
- `../interview_problems/original/01_applied_ai.md` - Practice problems 9-19
