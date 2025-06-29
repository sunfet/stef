from flask import Flask, jsonify

app = Flask(__name__, static_folder='static')

# 模拟游戏状态
game_state = {
    'current_floor': 0,
    'highest_floor': 0,
    'hero_count': 0,
    'gold': 0
}

@app.route('/')

def serve_index():
    return app.send_static_file('new_climb_tower_game.html')

@app.route('/game_state', methods=['GET'])



def get_game_state():
    return jsonify(game_state)

@app.route('/upgrade/<stat>', methods=['POST'])



def upgrade_stat(stat):
    if stat == 'health':
        # 处理生命值升级逻辑
        pass
    elif stat == 'attack':
        # 处理攻击力升级逻辑
        pass
    elif stat == 'defense':
        # 处理防御力升级逻辑
        pass
    elif stat == 'speed':
        # 处理爬塔速度升级逻辑
        pass
    return jsonify(game_state)

if __name__ == '__main__':
    app.run(debug=True)