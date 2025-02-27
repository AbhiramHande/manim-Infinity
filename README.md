# Infinity: Manim Animations for National Science Day 2025

This repository contains Manim animations created for a talk on *Infinity* that will be delivered by my professor, Dr. Shailesh Trivedi, on **National Science Day (28th Feb 2025)**. The talk aims to inspire students from **grades 8-11 in rural India** to pursue higher education in STEM. The animations illustrate fundamental concepts of infinity using mathematical visualization.

## Animations

Below are the key animations along with descriptions:

1. **Division by Zero Tends to Infinity:** Visualizes how $\frac{1}{0}, \frac{2}{0}, \frac{3}{0},$ etc., tend to positive infinity as x approaches 0 from the right.  
   ![Right Hand Limits](animations/MorphHyperbola.gif)

2. **When Are Two Sets of Equal Size?** Introduces the concept of *cardinality* and the idea of *one-to-one and onto correspondence*.  
   ![Cardinality](animations/Cardinality.gif)

3. **Defining an Infinite Set:** Demonstrates that a set is infinite if there is a bijection between it and one of its proper subsets.  
   ![Infinite Set](animations/InfiniteSet.gif)

4. **Bijection Between Natural Numbers and Even Numbers:** Shows a one-to-one correspondence between natural numbers and even numbers, illustrating that both have the same cardinality.  
   ![Bijection Natural and Even](animations/BijectionEven.gif)

5. **Bijection Between Natural Numbers and Natural Numbers Excluding One**  
   Illustrates a bijection between $N$ and $N \setminus \{1\}$, emphasizing that removing one element doesn’t change the size of an infinite set.  
   ![Bijection Natural and Natural numbers excluding One](animations/Bijection.gif)

6. **Sum of Infinite Numbers Need Not Be Infinite:** Explains how the infinite geometric series $\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots$ converges to 1.  
   ![Geometric Series Animation](animations/GeometricSeries.gif)

## Installation

To run these animations locally, you need to install [Manim](https://www.manim.community/)
```sh
pip install manim
```

You may also need to install these prerequisites:
1. **FFmpeg:** Required for video rendering.
```bash
sudo apt update
sudo apt install ffmpeg
```
2. **$\LaTeX$:** Required for rendering LaTeX texts.

## Running the Animations

You can render an animation using the following command:

```sh
manim -pql <filename.py>
```
   - `-p` is used to preview after rendering.
   - `-ql` is used for low quality fast render
   - Alternatively, `-qm` or `-qh` can also be used.

## Repository Structure

```
manim-Infinity
├── 📂 animations
├── 📂 src
├── README.md
└── License.txt
```

## License

This project is licensed under the MIT License.

---

