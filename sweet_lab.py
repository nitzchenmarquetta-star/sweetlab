#!/usr/bin/env python3
"""
甜蜜实验室 (Sweet Lab) - 主程序
"""

import sys
import argparse
from pathlib import Path

# 添加当前目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from core import PoemGenerator, LoveGenerator, LoveTester, ChatHelper, AvatarStyler, MoreInteractions


class SweetLab:
    """甜蜜实验室主类"""

    def __init__(self):
        self.poem_gen = PoemGenerator()
        self.love_gen = LoveGenerator()
        self.love_tester = LoveTester()
        self.chat_helper = ChatHelper()
        self.avatar_styler = AvatarStyler()
        self.more_interactions = MoreInteractions()
        print("=" * 50)
        print("🍬 甜蜜实验室 (Sweet Lab)")
        print("💕 甜蜜制造机，搞怪也甜蜜！")
        print("=" * 50)
        print()

    def run_poem(self, name: str, style: str = 'romantic'):
        """运行藏头诗生成"""
        print(f"📝 生成藏头诗 - 名字: {name}, 风格: {style}")
        print("-" * 50)

        result = self.poem_gen.generate_acrostic(name, style)

        if result.get('success'):
            print(f"✨ 风格: {result.get('style_name')}")
            print()
            print(result.get('poem'))
            print()
            if result.get('ending'):
                print(result.get('ending'))
            print()
            print("-" * 50)
            print("✅ 生成完成！")
        else:
            print(f"❌ 失败: {result.get('error')}")

    def run_love(self, style: str = 'romantic', 
                 name: str = '', scene: str = ''):
        """运行情话生成"""
        print(f"💕 生成情话 - 风格: {style}")
        if name:
            print(f"👤 名字: {name}")
        if scene:
            print(f"🎬 场景: {scene}")
        print("-" * 50)

        result = self.love_gen.generate(style, name, scene)

        if result.get('success'):
            print(f"✨ 风格: {result.get('style_name')}")
            print()
            print(result.get('text'))
            print()
            print("-" * 50)
            print("✅ 生成完成！")
        else:
            print(f"❌ 失败: {result.get('error')}")

    def run_test(self, name1: str, name2: str, 
                 birthday1: str = '', birthday2: str = '',
                 relationship_type: str = 'romantic'):
        """运行爱情测试"""
        print(f"💕 爱情测试 - {name1} & {name2}")
        print("-" * 50)

        result = self.love_tester.test(name1, name2, birthday1, birthday2, relationship_type)

        if result.get('success'):
            print(f"✨ {result.get('result')}")
            print()
            print(result.get('analysis'))
            print()
            print("-" * 50)
            print(f"分享文案: {result.get('share_text')}")
            print()
            print("✅ 测试完成！")
        else:
            print(f"❌ 失败: {result.get('error')}")

    def run_chat(self, message: str = '', style: str = 'normal',
                scene: str = '', earthy: bool = False):
        """运行聊天助手"""
        if earthy:
            print("😂 土味情话")
            print("-" * 50)
            result = self.chat_helper.generate_earthy_flirt(3)
            if result.get('success'):
                for i, flirt in enumerate(result.get('flirts'), 1):
                    print(f"{i}. {flirt}")
                print()
                print("-" * 50)
                print("✅ 生成完成！")
            return

        if message:
            print(f"💬 生成回复 - 消息: {message}")
            print("-" * 50)
            result = self.chat_helper.generate_reply(message, style)
            if result.get('success'):
                print(f"✨ 风格: {result.get('style_name')}")
                print()
                for i, reply in enumerate(result.get('replies'), 1):
                    print(f"{i}. {reply}")
                print()
                print("-" * 50)
                print("✅ 生成完成！")
            return

        if scene:
            print(f"🎯 话题开场白 - 场景: {scene}")
            print("-" * 50)
            result = self.chat_helper.generate_topic_starter(scene)
            if result.get('success'):
                print(f"✨ 场景: {result.get('scene_name')}")
                print()
                for i, starter in enumerate(result.get('starters'), 1):
                    print(f"{i}. {starter}")
                print()
                print("-" * 50)
                print("✅ 生成完成！")
            return

        print("请指定 --message, --scene 或 --earthy 参数！")

    def run_avatar(self, image_path: str, style: str = 'candy',
                    output_path: str = None):
        """运行头像风格化"""
        print(f"🎨 头像风格化 - {image_path}")
        print("-" * 50)

        result = self.avatar_styler.apply_style(image_path, style, output_path)

        if result.get('success'):
            print(f"✨ 风格: {result.get('style_name')}")
            print()
            print(f"✅ 处理完成！已保存到: {result.get('output_path')}")
        else:
            print(f"❌ 失败: {result.get('error')}")

    def run_interact(self, game_type: str, **kwargs):
        """运行互动游戏"""
        if game_type == 'couple_name':
            return self._run_couple_name(kwargs.get('name1'), kwargs.get('name2'))
        elif game_type == 'nickname':
            return self._run_nickname(kwargs.get('name'))
        elif game_type == 'truth_or_dare':
            return self._run_truth_or_dare(kwargs.get('choice'))
        elif game_type == 'lucky_draw':
            return self._run_lucky_draw()

    def _run_couple_name(self, name1: str, name2: str):
        """运行情侣名生成"""
        print(f"💕 情侣名生成 - {name1} & {name2}")
        print("-" * 50)

        result = self.more_interactions.generate_couple_name(name1, name2)

        if result.get('success'):
            print(f"✨ 情侣名: {result.get('couple_name')}")
            print()
            print("✅ 生成完成！")
        else:
            print(f"❌ 失败: {result.get('error')}")

    def _run_nickname(self, name: str):
        """运行外号生成"""
        print(f"😜 外号生成 - {name}")
        print("-" * 50)

        result = self.more_interactions.generate_nickname(name)

        if result.get('success'):
            print(f"✨ 外号: {result.get('nickname')}")
            print()
            print("✅ 生成完成！")
        else:
            print(f"❌ 失败: {result.get('error')}")

    def _run_truth_or_dare(self, choice: str):
        """运行真心话大冒险"""
        print(f"🎮 真心话大冒险")
        print("-" * 50)

        result = self.more_interactions.truth_or_dare(choice)

        if result.get('success'):
            print(f"✨ {result.get('type_name')}")
            print()
            print(result.get('content'))
            print()
            print("✅ 完成！")

    def _run_lucky_draw(self):
        """运行每日抽签"""
        print(f"🍀 每日抽签")
        print("-" * 50)

        result = self.more_interactions.lucky_draw()

        if result.get('success'):
            print(f"✨ {result.get('item')}")
            print()
            print("✅ 抽签完成！")

    def list_styles(self):
        """列出所有风格和游戏"""
        print("🎨 藏头诗风格:")
        for s in self.poem_gen.list_styles():
            print(f"  - {s['id']}: {s['name']}")

        print()
        print("💕 情话风格:")
        for s in self.love_gen.list_styles():
            print(f"  - {s['id']}: {s['name']}")

        print()
        print("🎬 情话场景:")
        for s in self.love_gen.list_scenes():
            print(f"  - {s['id']}: {s['name']}")

        print()
        print("💬 聊天回复风格:")
        for s in self.chat_helper.list_styles():
            print(f"  - {s['id']}: {s['name']}")

        print()
        print("🎯 聊天场景:")
        for s in self.chat_helper.list_scenes():
            print(f"  - {s['id']}: {s['name']}")

        print()
        print("🎨 头像风格:")
        for s in self.avatar_styler.list_styles():
            print(f"  - {s['id']}: {s['name']}")

        print()
        print("🎮 互动游戏:")
        for g in self.more_interactions.list_games():
            print(f"  - {g['id']}: {g['name']}")


def main():
    """主函数"""

    parser = argparse.ArgumentParser(
        description='🍬 甜蜜实验室 - 浪漫文案生成器',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s poem "小红"                      # 生成藏头诗
  %(prog)s poem "小明" --style cute         # 指定风格
  %(prog)s love                             # 生成情话
  %(prog)s love --style funny               # 搞笑风格
  %(prog)s love --name "小红"               # 带上名字
  %(prog)s test "小红" "小明"               # 爱情测试
  %(prog)s test "小红" "小明" --type friendship  # 友情测试
  %(prog)s chat --earthy                    # 土味情话
  %(prog)s chat --message "在干嘛" --style cute  # 生成回复
  %(prog)s chat --scene first_chat          # 话题开场白
  %(prog)s avatar "头像.png" --style candy # 头像风格化
  %(prog)s interact couple_name --name1 "小红" --name2 "小明"  # 情侣名生成
  %(prog)s interact nickname --name "小红"  # 外号生成
  %(prog)s interact truth_or_dare            # 真心话大冒险
  %(prog)s interact lucky_draw               # 每日抽签
  %(prog)s styles                           # 列出所有风格
        """
    )

    subparsers = parser.add_subparsers(title='命令', dest='command')

    # poem 命令
    poem_parser = subparsers.add_parser('poem', help='生成藏头诗')
    poem_parser.add_argument('name', help='名字（2-4字）')
    poem_parser.add_argument('--style', default='romantic',
                            help='风格（romantic/cute/funny/modern）')

    # love 命令
    love_parser = subparsers.add_parser('love', help='生成情话')
    love_parser.add_argument('--style', default='romantic',
                            help='风格（romantic/funny/cute/direct/literary）')
    love_parser.add_argument('--name', default='', help='对方名字（可选）')
    love_parser.add_argument('--scene', default='',
                            help='场景（first_meet/anniversary/confession/goodnight）')

    # styles 命令
    styles_parser = subparsers.add_parser('styles', help='列出所有风格')

    # test 命令
    test_parser = subparsers.add_parser('test', help='爱情/友情测试')
    test_parser.add_argument('name1', help='第一个人的名字')
    test_parser.add_argument('name2', help='第二个人的名字')
    test_parser.add_argument('--birthday1', default='', help='第一个人生日（可选）')
    test_parser.add_argument('--birthday2', default='', help='第二个人生日（可选）')
    test_parser.add_argument('--type', default='romantic',
                           help='关系类型（romantic/friendship）')

    # chat 命令
    chat_parser = subparsers.add_parser('chat', help='聊天话术助手')
    chat_parser.add_argument('--message', default='', help='对方说的话')
    chat_parser.add_argument('--style', default='normal',
                           help='回复风格（flirty/cute/funny/normal）')
    chat_parser.add_argument('--scene', default='',
                           help='场景（first_chat/ambiguous/couple）')
    chat_parser.add_argument('--earthy', action='store_true', help='土味情话')

    # avatar 命令
    avatar_parser = subparsers.add_parser('avatar', help='头像风格化')
    avatar_parser.add_argument('image', help='输入图片路径')
    avatar_parser.add_argument('--style', default='candy',
                             help='风格（candy/anime/vintage/ins/sketch）')
    avatar_parser.add_argument('--output', default='', help='输出图片路径（可选）')

    # interact 命令
    interact_parser = subparsers.add_parser('interact', help='互动游戏')
    interact_parser.add_argument('game', help='游戏类型（couple_name/nickname/truth_or_dare/lucky_draw）')
    interact_parser.add_argument('--name1', default='', help='第一个人的名字（情侣名用）')
    interact_parser.add_argument('--name2', default='', help='第二个人的名字（情侣名用）')
    interact_parser.add_argument('--name', default='', help='名字（外号用）')
    interact_parser.add_argument('--choice', default='random', help='选择（truth/dare/random，真心话大冒险用）')

    args = parser.parse_args()

    lab = SweetLab()

    if args.command == 'poem':
        lab.run_poem(args.name, args.style)
    elif args.command == 'love':
        lab.run_love(args.style, args.name, args.scene)
    elif args.command == 'styles':
        lab.list_styles()
    elif args.command == 'test':
        lab.run_test(args.name1, args.name2, args.birthday1, args.birthday2, args.type)
    elif args.command == 'chat':
        lab.run_chat(args.message, args.style, args.scene, args.earthy)
    elif args.command == 'avatar':
        lab.run_avatar(args.image, args.style, args.output)
    elif args.command == 'interact':
        lab.run_interact(args.game,
                        name1=args.name1, name2=args.name2,
                        name=args.name, choice=args.choice)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
