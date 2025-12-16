from models.team_dto import TeamDTO
from models.team_entity import TeamEntity


def team_dto_to_entity(team_dto: TeamDTO) -> TeamEntity:
    return TeamEntity(sk=team_dto.team_id, team_name=team_dto.team_name, team_color=team_dto.team_color)

def team_entity_to_dto(team_entity: TeamEntity) -> TeamDTO:
    return TeamDTO(team_id=team_entity.sk, team_name=team_entity.team_name, team_color=team_entity.team_color)