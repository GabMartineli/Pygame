
from codegame.const import ENTITY_ATTACK, WIN_WIDTH
from codegame.enemy import Enemy
from codegame.enemyShot import EnemyShot
from codegame.entity import Entity
from codegame.player import Player
from codegame.playerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

        pass

    @staticmethod
    def verify_collision_entity(ent1, ent2):
        collision = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            collision = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            collision = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            collision = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            collision = True

        if collision == True:
            if (ent1.rect.right >= ent2.rect.left 
                    and ent1.rect.left <= ent2.rect.right 
                    and ent1.rect.bottom >= ent2.rect.top 
                    and ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.attack
                ent2.health -= ent1.attack
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

        pass

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.verify_collision_window(entity1)
            for j in range(i+1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.verify_collision_entity(entity1, entity2)
        pass

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.score(ent, entity_list)
                entity_list.remove(ent)

    @staticmethod
    def score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg in ['Player1Shot', 'Player2Shot', 'Player3Shot']:
            for ent in entity_list:
                if ent.name in ['Player1', 'Player2', 'Player3']:
                    ent.score += enemy.score