from visualaid import Grid, Animator
from random import randrange


def animate_dots(old_dots, new_dots, delta_x, delta_y):
    print(f"Animating Fold: {fold_count}/{len(fold_instructions)}")
    animation_frames = 1
    prev_frame_dots = []
    moving_color_map = dot_color_map.copy()
    while new_dots != old_dots:
        for dot in old_dots:
            if dot in prev_frame_dots:
                g.fill_cell(dot, fill=(0, 0, 0))
        prev_frame_dots = []
        for i, dot in enumerate(old_dots):
            if old_dots[i] != new_dots[i]:
                new_dot = (dot[0] - delta_x, dot[1] - delta_y)
                old_dots[i] = new_dot
                moving_color_map[new_dot] = moving_color_map[dot]

        for dot in old_dots:
            if dot not in new_dots:
                g.fill_cell(
                    dot,
                    fill=moving_color_map[dot],
                )
                prev_frame_dots.append(dot)
            else:
                g.fill_cell(dot, fill=dot_color_map[dot])
        if not animation_frames % (15 - fold_count):
            g.save_frame()
        animation_frames += 1


def fold_grid(fold_instruction, dots):
    global dot_color_map
    fold_line = int(fold_instruction.split("=")[1])
    print(f"Folding: {fold_count}/{len(fold_instructions)}")
    if "y" in fold_instruction:
        delta_y = 1
        delta_x = 0
    else:
        delta_x = 1
        delta_y = 0

    new_dots = []
    for dot in dots:
        if delta_x and dot[0] > fold_line:
            new_dot = (dot[0] - (2 * abs(dot[0] - fold_line)), dot[1])
        elif delta_y and dot[1] > fold_line:
            new_dot = (dot[0], dot[1] - (2 * abs(dot[1] - fold_line)))
        else:
            new_dot = dot
        dot_color_map[new_dot] = dot_color_map[dot]

        new_dots.append(new_dot)

    animate_dots(dots, new_dots.copy(), delta_x, delta_y)
    return list(set(new_dots))


with open("input.txt") as f:
    data = [l.strip() for l in f.readlines()]

dots = [tuple(map(int, i)) for i in [d.split(",") for d in data if "," in d]]
dot_color_map = {
    dot: (randrange(50, 255), randrange(50, 255), randrange(50, 255)) for dot in dots
}
fold_instructions = [i.split()[-1] for i in data if "=" in i]

fold_count = 1
grids = []
for i, fold_instruction in enumerate(fold_instructions):
    g = Grid(
        max([d[0] for d in dots]) + 1,
        max([d[1] for d in dots]) + 1,
        2 * fold_count,
        2 * fold_count,
        bg_color=(0, 0, 0),
        frame_counter_text=True,
    )
    g.frame_counter_text_color = (128, 128, 128)
    for dot in dots:
        g.fill_cell(dot, fill=dot_color_map[dot])
    g.save_frame()
    for dot in dots:
        g.fill_cell(dot, fill=(0, 0, 0))
    dots = fold_grid(fold_instruction, dots)
    for dot in dots:
        g.fill_cell(dot, fill=dot_color_map[dot])
    g.save_frame()
    fold_count += 1
    # if i < len(fold_instructions) - 1:
    grids.append(g)
animator = Animator()
animator.save_animation(
    grids,
    filename=f"test_animator.gif",
    duration=50,
    holdresult=3000,
    resize=(800, 800),
)
