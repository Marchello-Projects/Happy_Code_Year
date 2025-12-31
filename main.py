import colorsys
import math
import random
import sys

import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy New Year Coding!")

BLACK = (10, 10, 30)
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
DARK_GREEN = (0, 100, 0)
WOOD = (139, 69, 19)

snowflakes = []
for _ in range(200):
    x = random.randrange(0, WIDTH)
    y = random.randrange(0, HEIGHT)
    speed = random.randrange(1, 4)
    size = random.randrange(2, 5)
    snowflakes.append([x, y, speed, size])

try:
    font_title = pygame.font.SysFont("arial", 70, bold=True)
    font_toys = pygame.font.SysFont("comicsansms", 20, bold=True)
except:
    font_title = pygame.font.Font(None, 70)
    font_toys = pygame.font.Font(None, 20)

tree_segments = [
    [(WIDTH // 2, 140), (WIDTH // 2 - 60, 260), (WIDTH // 2 + 60, 260)],
    [(WIDTH // 2, 260), (WIDTH // 2 - 120, 420), (WIDTH // 2 + 120, 420)],
    [(WIDTH // 2, 420), (WIDTH // 2 - 180, 580), (WIDTH // 2 + 180, 580)],
]

toys_data = [
    {"text": "JAVA", "pos": (WIDTH // 2, 230), "color": (200, 50, 50)},
    {"text": "JS", "pos": (WIDTH // 2 - 40, 330), "color": (247, 223, 30)},
    {"text": "TS", "pos": (WIDTH // 2 + 40, 330), "color": (0, 122, 204)},
    {"text": "GO", "pos": (WIDTH // 2, 380), "color": (0, 173, 216)},
    {"text": "PYTHON", "pos": (WIDTH // 2, 470), "color": (55, 118, 171)},
    {"text": "C++", "pos": (WIDTH // 2 - 70, 500), "color": (0, 66, 128)},
    {"text": "RUST", "pos": (WIDTH // 2 + 70, 500), "color": (222, 60, 0)},
    {"text": "SWIFT", "pos": (WIDTH // 2 - 110, 540), "color": (240, 81, 56)},
    {"text": "PHP", "pos": (WIDTH // 2 + 110, 540), "color": (119, 123, 179)},
    {"text": "SQL", "pos": (WIDTH // 2, 540), "color": (100, 100, 100)},
]

lights = []
for _ in range(50):
    lx = random.randint(WIDTH // 2 - 150, WIDTH // 2 + 150)
    ly = random.randint(160, 560)
    if abs(lx - WIDTH // 2) < (ly - 100) * 0.45:
        lights.append(
            [
                lx,
                ly,
                random.choice(
                    [
                        (255, 0, 0),
                        (0, 255, 0),
                        (0, 0, 255),
                        (255, 255, 0),
                        (255, 0, 255),
                    ]
                ),
            ]
        )

hue = 0
star_pulse = 0
clock = pygame.time.Clock()


def draw_tree():
    pygame.draw.rect(SCREEN, WOOD, (WIDTH // 2 - 25, 580, 50, 20))
    for segment in tree_segments:
        pygame.draw.polygon(SCREEN, GREEN, segment)
        pygame.draw.polygon(SCREEN, DARK_GREEN, segment, 3)


def draw_snow():
    for flake in snowflakes:
        pygame.draw.circle(SCREEN, WHITE, (flake[0], flake[1]), flake[3])
        flake[1] += flake[2]
        flake[0] += random.choice([-1, 0, 1])
        if flake[1] > HEIGHT:
            flake[1] = random.randrange(-20, -5)
            flake[0] = random.randrange(0, WIDTH)


def draw_lights():
    for light in lights:
        if random.randint(0, 30) == 0:
            light[2] = (
                random.randint(100, 255),
                random.randint(100, 255),
                random.randint(100, 255),
            )
        pygame.draw.circle(SCREEN, light[2], (light[0], light[1]), 4)


def draw_toys():
    for toy in toys_data:
        text_color = (0, 0, 0) if toy["text"] == "JS" else (255, 255, 255)
        text_surf = font_toys.render(toy["text"], True, text_color)
        text_rect = text_surf.get_rect(center=toy["pos"])

        radius = max(text_rect.width, text_rect.height) // 2 + 8
        pygame.draw.circle(SCREEN, toy["color"], toy["pos"], radius)
        pygame.draw.circle(
            SCREEN,
            (255, 255, 255),
            (toy["pos"][0] - radius // 3, toy["pos"][1] - radius // 3),
            3,
        )
        pygame.draw.circle(SCREEN, (30, 30, 30), toy["pos"], radius, 1)
        SCREEN.blit(text_surf, text_rect)


def draw_star(pulse):
    cx, cy = WIDTH // 2, 115
    size = 22 + int(5 * abs(math.sin(pulse)))

    points = [
        (cx, cy - size),
        (cx + size * 0.4, cy - size * 0.3),
        (cx + size, cy),
        (cx + size * 0.4, cy + size * 0.3),
        (cx, cy + size),
        (cx - size * 0.4, cy + size * 0.3),
        (cx - size, cy),
        (cx - size * 0.4, cy - size * 0.3),
    ]

    pygame.draw.polygon(SCREEN, (255, 215, 0), points)
    pygame.draw.polygon(SCREEN, (255, 255, 255), points, 2)

    code_font = pygame.font.SysFont("consolas", 20, bold=True)
    code_text = code_font.render("</>", True, (40, 40, 40))
    SCREEN.blit(code_text, code_text.get_rect(center=(cx, cy)))


def draw_title(h_value):
    rgb = colorsys.hsv_to_rgb(h_value, 1, 1)
    color = tuple(int(c * 255) for c in rgb)

    text = "HAPPY NEW YEAR!"
    text_surf = font_title.render(text, True, color)
    text_rect = text_surf.get_rect(center=(WIDTH // 2, 45))

    shadow = font_title.render(text, True, (80, 80, 80))
    SCREEN.blit(shadow, (text_rect.x + 4, text_rect.y + 4))
    SCREEN.blit(text_surf, text_rect)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill(BLACK)

    draw_star(star_pulse)
    draw_snow()
    draw_tree()
    draw_lights()
    draw_toys()

    star_pulse += 0.08

    hue += 0.005
    if hue > 1:
        hue = 0
    draw_title(hue)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()