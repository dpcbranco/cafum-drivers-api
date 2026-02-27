from models.driver_results.driver_result_dto import DriverResultDTO
from models.grands_prix.gp_dto import GrandPrixDto
from models.grands_prix.gp_entity import GrandPrixEntity
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

def gp_entity_to_dto(gp_entity: GrandPrixEntity) -> GrandPrixDto:
    return GrandPrixDto(
        grand_prix_id=gp_entity.sk,
        year=int(gp_entity.pk.split("#")[1]),
        name=gp_entity.name,
        quali_bet_limit_date=gp_entity.quali_bet_limit_date,
        race_bet_limit_date=gp_entity.race_bet_limit_date,
        quali_result=gp_entity.quali_result,
        race_result=gp_entity.race_result
    )

def gp_dto_to_entity(gp_dto: GrandPrixDto) -> GrandPrixEntity:
    return GrandPrixEntity(
        pk=f'RACE#{gp_dto.year}',
        sk=gp_dto.grand_prix_id,
        name=gp_dto.name,
        quali_bet_limit_date=gp_dto.quali_bet_limit_date,
        race_bet_limit_date=gp_dto.race_bet_limit_date,
        quali_result={key: value.to_dict() for key, value in gp_dto.quali_result.items()},
        race_result={key: value.to_dict() for key, value in gp_dto.race_result.items()}
    )