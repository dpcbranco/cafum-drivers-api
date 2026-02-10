from models.teams.team_dto import TeamDTO
from models.teams.team_entity import TeamEntity


def team_dto_to_entity(team_dto: TeamDTO) -> TeamEntity:
    return TeamEntity(
        sk=team_dto.team_id,
        team_name=team_dto.team_name,
        team_color=team_dto.team_color,
        first_driver=team_dto.first_driver.to_dict(),
        second_driver=team_dto.second_driver.to_dict()
    )

def team_entity_to_dto(team_entity: TeamEntity) -> TeamDTO:
    return TeamDTO(
        team_id=team_entity.sk,
        team_name=team_entity.team_name,
        team_color=team_entity.team_color,
        first_driver=team_entity.first_driver,
        second_driver=team_entity.second_driver
    )
