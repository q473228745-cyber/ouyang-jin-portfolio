import re

# 定义所有需要修复的文件
files = {
    'index': r'C:\Users\Administrator\Desktop\portfolio-website\index.html',
    'case-01': r'C:\Users\Administrator\Desktop\portfolio-website\pages\case-01.html',
    'case-02': r'C:\Users\Administrator\Desktop\portfolio-website\pages\case-02.html',
    'case-03': r'C:\Users\Administrator\Desktop\portfolio-website\pages\case-03.html',
    'case-04': r'C:\Users\Administrator\Desktop\portfolio-website\pages\case-04.html',
    'case-05': r'C:\Users\Administrator\Desktop\portfolio-website\pages\case-05.html',
}

# Figma 原型链接占位符
FIGMA_PLACEHOLDER = 'https://www.figma.com/proto/your-prototype-link'

fixes_applied = []

for name, path in files.items():
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # P0-1: 修复 CTA 按钮的 href="#" → 真实链接占位符
    if 'class="cta-btn"' in content:
        content = content.replace('href="#" class="cta-btn"', f'href="{FIGMA_PLACEHOLDER}" class="cta-btn"')
        if content != original:
            fixes_applied.append(f'{name}: CTA 按钮链接已修复')
    
    # P0-2: 修复首页 logo href="#" 
    if name == 'index':
        # Logo 链接已经修复为 #hero
        pass
    
    # P0-4: 修复 Case 04 封面副标题英文
    if name == 'case-04':
        content = content.replace(
            'Service system optimization for urban bus terminal information experience.',
            '城市公交枢纽信息服务系统优化设计'
        )
        if content != original:
            fixes_applied.append('case-04: 封面副标题已改为中文')
    
    # P0-5: 修复 Case 05 封面副标题英文
    if name == 'case-05':
        content = content.replace(
            'Digital experience design for intangible cultural heritage — Guqin music and Chinese Opera.',
            '非遗文化的数字化体验设计 — 古琴与戏曲'
        )
        if content != original:
            fixes_applied.append('case-05: 封面副标题已改为中文')
    
    # 保存修改后的文件
    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'✓ {name}: 已保存修改')

print('\n=== 修复总结 ===')
for fix in fixes_applied:
    print(f'  • {fix}')
