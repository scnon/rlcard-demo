from .env import Env

def register():
    from rlcard.envs.registration import register, make
    register(
        env_id='sichuan_mahjong',
        entry_point='sichuan_mahjong:Env',
    )

register()
