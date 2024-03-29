from app.entities.agent_data import AgentData
from app.entities.processed_agent_data import ProcessedAgentData


def process_agent_data(
    agent_data: AgentData,
) -> ProcessedAgentData:
    """
    Process agent data and classify the state of the road surface.
    Parameters:
        agent_data (AgentData): Agent data that containing accelerometer, GPS, and timestamp.
    Returns:
        processed_data_batch (ProcessedAgentData): Processed data containing the classified state of the road surface and agent data.
    """

    z = agent_data.accelerometer.z
    deviation = abs(z - 16500)
    if deviation <= 100:
        state = "GOOD"
    elif (deviation > 100) and (deviation <= 400):
        state = "BAD"
    else:
        state = "DANGEROUS"

        
    return ProcessedAgentData(
                            road_state=state,
                            agent_data=agent_data
                            )
