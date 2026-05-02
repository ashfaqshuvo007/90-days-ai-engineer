## To-do List

- Run the OpenAI/Anthropic quickstarts (Python & JS). - Using GEMINI instead
- Send a message, stream it, mess with temperature/top_p, hit a rate limit, parse an error.
- Force JSON output using the `response_format` parameter (or tool calling with strict: true). Write a script that asks for a fictional invoice and stores the parsed JSON in a dict. Intentionally prompt it to break the schema and catch the failure.

**With Low Temperature - 0.1**

```text
To understand how Artificial Intelligence (AI) works, it helps to stop thinking of it as a "robot brain" and start thinking of it as **extremely advanced pattern recognition.**

At its core, AI is a blend of math, data, and computer science. Here is the step-by-step breakdown of how it functions.

---

### 1. The Foundation: Data (The Fuel)
AI cannot think for itself; it learns from information. To build an AI, you must feed it massive amounts of data.
*   **For a Chatbot:** It reads billions of pages of text (books, websites, articles).
*   **For Image Recognition:** It looks at millions of labeled photos (e.g., "this is a cat," "this is a car").
*   **For Self-Driving Cars:** It processes thousands of hours of driving footage and sensor data.

### 2. The Engine: Algorithms and Models
An **algorithm** is a set of instructions. In traditional computing, a human writes every rule (e.g., "If the user clicks this, do that").

In AI, we use **Machine Learning**. Instead of writing specific rules, we give the computer an algorithm that allows it to *create its own rules* based on the data it sees. The result of this process is called a **Model.**

### 3. The Structure: Neural Networks
Most modern AI (like ChatGPT or Midjourney) uses **Neural Networks**. These are mathematical structures inspired by the human brain.
*   **Layers:** A neural network consists of layers of "neurons" (code).
*   **Processing:** When data enters the network, it passes through these layers. Each layer identifies different features.
    *   *Example:* If an AI is looking at a photo of a face, the first layer might find lines, the second layer finds shapes (eyes/nose), and the final layer recognizes the whole face.

### 4. The Process: Training and Feedback
This is where the "learning" happens. It involves a cycle of trial and error:
1.  **Prediction:** The AI is shown a piece of data and asked to guess what it is.
2.  **Error Calculation:** If the AI guesses "Dog" but the image is a "Cat," the system calculates how far off it was.
3.  **Adjustment:** The AI adjusts its internal connections (called **weights**) to be more accurate next time.

This happens millions of times until the AI becomes incredibly accurate at predicting the correct output.

### 5. The Result: Inference
Once the AI is trained, it enters the **Inference** stage. This is when you use it. When you ask ChatGPT a question, it isn't "looking up" an answer in a database. Instead, it is using the patterns it learned during training to **predict** which words should come next in a sentence, one by one, based on probability.

---

### A Simple Analogy: Learning to Bake
*   **Traditional Programming:** A recipe book. You follow the exact steps to get a cake. If a step is missing, you get stuck.
*   **Artificial Intelligence:** You are given 1,000 cakes and 1,000 "not-cakes." You taste them all, look at the ingredients, and eventually, you figure out the "pattern" of what makes a cake. Now, if someone gives you flour and eggs, you know what to do without needing the recipe book.

---

### Summary: Why is it so powerful now?
AI has been around since the 1950s, but it has exploded recently for three reasons:
1.  **Big Data:** We finally have enough digital information to feed the models.
2.  **Computing Power:** We have powerful chips (GPUs) that can handle the massive math required.
3.  **Better Math:** Scientists have discovered more efficient ways to structure neural networks (like the "Transformer" architecture that powers ChatGPT).

**The most important thing to remember:** AI doesn't "understand" things the way humans do. It doesn't have feelings or consciousness. It is simply a very sophisticated calculator that predicts the most likely outcome based on what it has seen before.
```

**With High Temperature**

```text
At its simplest level, Artificial Intelligence (AI) doesn't "think" the way a human does. It doesn't have feelings, beliefs, or a conscious mind. Instead, it is a highly sophisticated system of **mathematics, data, and pattern recognition.**

Here is a breakdown of how AI works, from the basic building blocks to the complex systems we use today.

---

### 1. The Core Ingredient: Data
AI runs on data. Just as a human learns from experiences, an AI learns from information. This data can be text (books, websites), images, numbers, or even sounds.
*   **The Volume:** To make an AI smart, you need massive amounts of data.
*   **The Goal:** The AI looks at this data to find **patterns**. For example, if you show an AI 10,000 photos of cats, it begins to notice that "cats" usually have pointy ears, whiskers, and a specific eye shape.

### 2. The Engine: Machine Learning (ML)
Machine Learning is the most common type of AI today. In traditional computer programming, a human writes specific "If/Then" rules (e.g., *"If the user clicks this button, then open this file"*).

In **Machine Learning**, the human doesn't give the rules. Instead, they give the AI the data and an objective, and the AI **figures out the rules for itself.**

There are three main ways it learns:
*   **Supervised Learning:** You give the AI labeled data (e.g., "This is a picture of a cat; this is a picture of a car"). It learns to associate labels with features.
*   **Unsupervised Learning:** You give the AI raw data and ask it to find patterns on its own (e.g., "Group these millions of customers into three categories based on their shopping habits").
*   **Reinforcement Learning:** The AI learns through trial and error. It gets a "reward" (a numerical score) when it does something right and a penalty when it does something wrong (this is how AI learns to play video games or chess).

### 3. The Architecture: Neural Networks
Modern AI (like ChatGPT or facial recognition) uses a structure called a **Neural Network**, which is loosely inspired by the human brain.

*   **Layers:** A neural network consists of layers of "neurons" (mathematical functions).
*   **Processing:** When information enters the network (like an image), the first layer identifies simple things (edges and lines). The next layer identifies shapes (circles or squares). The final layers identify complex objects (a human face).
*   **Weights:** As the AI learns, it adjusts the "weight" (importance) of different connections. If it's trying to identify a bird, it learns to give more weight to "feathers" and less weight to "color."

### 4. The Process: Training vs. Inference
AI work happens in two distinct stages:
1.  **Training:** This is the "schooling" phase. The AI is run on powerful computers (GPUs) for weeks or months, processing billions of data points until it becomes accurate.
2.  **Inference:** This is the "test" phase. Once the AI is trained, it is deployed to your phone or computer. When you ask it a question, it uses its "learned" patterns to provide an answer. This happens in seconds.

### 5. How Generative AI (like ChatGPT) Works
Generative AI is a specific type of AI that creates new content.
*   **Probability:** When you type a prompt into ChatGPT, it isn't "looking up" an answer in a database. It is calculating the **statistical probability** of which word should come next.
*   **Example:** If you type "The cat sat on the...", the AI calculates that "mat" is 80% likely, "floor" is 15% likely, and "refrigerator" is 1% likely. It chooses the most likely word and repeats the process for the next word.

### 6. The "Black Box" Problem
One of the most interesting (and scary) things about AI is that even the people who build it don't always know *exactly* why an AI made a specific decision. Because the AI creates its own rules based on billions of mathematical variables, it becomes a "Black Box"—we see what goes in and what comes out, but the internal "reasoning" is too complex for a human to track.

### Summary
*   **Data** is the fuel.
*   **Algorithms** are the engine.
*   **Neural Networks** are the structure.
*   **Pattern Recognition** is the result.

AI is essentially **a giant prediction machine** that uses the past (data) to make guesses about the present or future.
```

```json
{
  "recipe_name": "Delicious Chocolate Chip Cookies",
  "ingredients": [
    {
      "name": "all-purpose flour",
      "quantity": "2 and 1/4 cups"
    },
    {
      "name": "baking soda",
      "quantity": "1 teaspoon"
    },
    {
      "name": "salt",
      "quantity": "1 teaspoon"
    },
    {
      "name": "unsalted butter (softened)",
      "quantity": "1 cup"
    },
    {
      "name": "granulated sugar",
      "quantity": "3/4 cup"
    },
    {
      "name": "packed brown sugar",
      "quantity": "3/4 cup"
    },
    {
      "name": "vanilla extract",
      "quantity": "1 teaspoon"
    },
    {
      "name": "large eggs",
      "quantity": "2"
    },
    {
      "name": "semisweet chocolate chips",
      "quantity": "2 cups"
    }
  ],
  "instructions": [
    "Preheat the oven to 375°F (190°C).",
    "In a small bowl, whisk together the flour, baking soda, and salt.",
    "In a large bowl, cream together the butter, granulated sugar, and brown sugar until light and fluffy.",
    "Beat in the vanilla and eggs, one at a time.",
    "Gradually beat in the dry ingredients until just combined.",
    "Stir in the chocolate chips.",
    "Drop by rounded tablespoons onto ungreased baking sheets and bake for 9 to 11 minutes."
  ]
}
```
