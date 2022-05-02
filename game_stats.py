class ClassStats:
    """跟踪游戏统计信息"""

    def __init__(self,ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运行期间可能面临的问题"""
        self.ships_left = self.settings.ship_limit
        