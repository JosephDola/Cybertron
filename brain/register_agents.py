from brain.agent_registry import registry

from brain.agents.conversation_agent import conversation_agent

from brain.agents.software_agent import software_agent


registry.register(

    conversation_agent

)

registry.register(

    software_agent

)
