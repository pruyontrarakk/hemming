# Skyla Cui sc5146
# Patarada Yontrarak ppy2104

import time
from flask import Flask
from flask import render_template, Response, request, jsonify, url_for, redirect


app = Flask(__name__)

hem_steps = [
    {
        "title": "Introduction to Hemming",
        "images": ["1.1.png", "1.2.png"],
        "html": """
        <p><strong>What is hemming?</strong><br>
        A technique to finish the edge of fabric to prevent fraying and give a clean look.</p>
        <p><strong>When do you hem?</strong><br>
        Shortening garments, finishing handmade items, adjusting curtains, etc.</p>
        <p><strong>Why hand stitch your hem?</strong><br>
        More control, invisible finishes, great for delicate or thick fabrics.</p>
        """
    },
    {
        "title": "Tools You'll Need to Hem",
        "images": ["2.1.png"],
        "html": """
        <ul>
            <li>Needle (sharp, small-eyed)</li>
            <li>Thread (matching the fabric color)</li>
            <li>Pins or clips</li>
            <li>Scissors</li>
            <li>Measuring tape</li>
            <li>Iron (optional but recommended)</li>
        </ul>
        """
    },
    {
        "title": "Step 1: Mark your hemline with chalk or pins",
        "images": ["3.1.png"],
        "instructions": [
            "Try on the garment and make a small mark for approximate length",
            "Use chalk or pins to create a visible, removable guide",
            "Mark evenly across the full width for a straight hem",
            "Double-check that the marked hemline is level",
            "Try on the garment and check the length"
        ]
    },
    {
        "title": "Step 2: Fold up the raw edge once (¼”–½”) and press",
        "images": ["4.1.png"],
        "instructions": [
            "Fold up the raw edge by ¼–½ inch",
            "Use a measuring tape for consistency across the garment",
            "Press to set the fold and keep fabric from shifting, using an iron if needed",
            "Make sure all of the raw edge is hidden for a clean finish"
        ]
    },
    {
        "title": "Step 3: Fold again to desired hem depth and press",
        "images": ["5.1.png"],
        "instructions": [
            "Fold to the final hem depth (e.g., 1–2 inches)",
            "Match the hemline to your original markings from part 1",
            "Press firmly to crease the fold cleanly, using an iron if needed",
            "Take care to align any curves or seams"
        ]
    },
    {
        "title": "Step 4: Pin in place to secure",
        "images": ["6.1.png"],
        "instructions": [
            "Pin horizontally and evenly along the fold",
            "This step secures everything before stitching begins",
            "Now you’re ready to start sewing!"
        ]
    },

    {
        "title": "Choosing your hemming stitch type (Backstitch vs Slip stitch)",
        "images": [],
        "html": """
        <div style="display: flex; gap: 4rem;">
            <div>
                <strong>Why Backstitch</strong>
                <ul>
                    <li>Provides one of the strongest, most durable seams in hand sewing</li>
                    <li>Ideal for structural seams (e.g. garment construction, bag straps, repairs)</li>
                    <li>Cleaner and tighter, which are better for edges</li>
                    <li>Machine-like finish without using a machine</li>
                </ul>
            </div>
            <div>
                <strong>Slip stitch</strong>
                <ul>
                    <li>Nearly invisible on the outside — perfect for clean, professional-looking hems</li>
                    <li>Ideal for finishing hems on dress pants, skirts, formalwear, and curtains</li>
                    <li>Great for delicate or lightweight fabrics</li>
                    <li>Flexible and forgiving — allows the hem to move naturally without puckering</li>
                </ul>
            </div>
        </div>
        """
    },
    {
        "title": "How to Identify (Backstitch vs Slip stitch)",
        "images": ["8.1.png", "8.2.png", "8.3.png", "8.4.png"],
        "html": """
        <div style="display: flex; gap: 4rem;">
            <div>
                <strong>Backstitch</strong><br><br>
                <em>Frontside:</em><br>
                <p>A solid, continuous line of stitching that resembles machine sewing, with no gaps between stitches.</p>
                <em>Backside:</em><br>
                <p>A series of overlapping or slightly offset stitches, creating a somewhat dashed or broken line effect.</p>
            </div>
            <div>
                <strong>Slip stitch</strong><br><br>
                <em>Frontside:</em><br>
                <p>Nearly invisible, with only small, evenly spaced out stitches.</p>
                <em>Backside:</em><br>
                <p>Thread travels hidden within the hem fold, creating a long horizontal stitch line.</p>
            </div>
        </div>
        """
    }
]

backstitch_steps = [
    {
        "title": "Step 1: Thread the needle",
        "media": ["1.1.png", "1.2.mov"],
        "instructions": [
            "Make sure to use a thread that is a similar color to the fabric for a seamless look",
            "Tie a knot on one end of the thread after threading the needle"
        ]
    },
    {
        "title": "Step 2: The starting stitch",
        "media": ["2.1.png", "2.2.png", "2.3.mov"],
        "instructions": [
            "Place needle through fabric from underneath",
            "Thread it to the back (the right side of the original stitch) and then up in front (on the left side of the original stitch)"
        ]
    },
    {
        "title": "Step 3: Stitching backwards (repeat this step until complete)",
        "media": ["3.1.png", "3.2.png", "3.3.png", "3.4.mov", "3.5.mov"],
        "instructions": [
            "Loop the thread back to the stitch on the right and up again forward an equal distance",
            "Keep the distance between each of the individual stitches the same",
            "Continue in a straight line"
        ]
    },
    {
        "title": "Step 4: Tie knot at the end",
        "media": ["4.1.png", "4.2.png", "4.3.mov"],
        "instructions": [
            "Loop the thread through a small part of fabric",
            "Tie a knot before pulling all the way",
            "Pull on the knot and allow all thread to go through"
        ]
    }
]

slipstitch_steps = [
    {
        "title": "Step 1: Thread the needle",
        "media": ["1.1.png", "1.2.mov"],
        "instructions": [
            "Make sure to use a thread that is a similar color to the fabric for a seamless look",
            "Tie a knot on one end of the thread after threading thread onto the needle"
        ]
    },
    {
        "title": "Step 2: Tiny Stitch in Outer Fabric",
        "media": ["2.1.mov", "2.2.mov"],
        "instructions": [
            "Insert the needle through the fabric.",
            "Take a small horizontal stitch (just 1–2 threads deep) from the main fabric, just above the folded edge.",
            "Make sure the distance between the previous stitch and this one is very small.",
            "This is the part of the slip stitch that takes the most precision!"
        ]
    },
    {
        "title": "Step 3: Slide Needle Inside the Fold",
        "media": ["3.1.png", "3.2.mov"],
        "instructions": [
            "Insert the needle into the fold directly across from where it exited, and run it ¼–½ inch through the fold before coming out.",
            "This allows the thread to stay hidden in the back of the fabric."
        ]
    },
    {
        "title": "Step 4: Repeat!",
        "media": ["4.1.png"],
        "instructions": [
            "Repeat steps 2 and 3 until you reach the end!"
        ]
    },
    {
        "title": "Step 5: Tie knot at the end",
        "media": ["5.1.png", "5.2.png", "5.3.mov"],
        "instructions": [
            "Loop the thread through a small part of fabric",
            "Tie a knot before pulling all the way",
            "Pull on the knot and all all thread to go through"
        ]
    },
]

quiz_questions = {
    "1": {
        "text": "What does a backstitch look like on the front side of the fabric?",
        "choices": [
            "A dashed line",
            "A zigzag pattern",
            "A solid, continuous line of stitching",
            "Random loops and knots"
        ],
        "answer": 2,
        "images": [],                # e.g. ["1.1.png","1.2.png"]
        "explanation": {
            "correct":   "The front of a backstitch should be a solid, continuous line of stitching.",
            "incorrect": "Not quite—a backstitch front looks like a solid, continuous line."
        },
        "explanation_images": ["1.1-2.1.png"]     # e.g. ["1_exp.png"]
    },
    "2": {
        "text": "Why is backstitch strong?",
        "choices": [
            "It uses thicker thread",
            "It has overlapping stitches that form a solid line",
            "It’s sewn with a machine",
            "It uses double the fabric"
        ],
        "answer": 1,
        "images": [],
        "explanation": {
            "correct":   "It’s the overlapping stitches that interlock and give strength.",
            "incorrect": "The correct answer is: It has overlapping stitches that form a solid line. Since all of the stitches connect to the previous one, it creates a very strong structure. Backstitching does not require a sewing machine."
        },
        "explanation_images": ["1.1-2.1.png"]
    },
    "3": {
        "text": "Which step of back stitching does this photo illustrate?",
        "choices": [
            "Preparing the thread and tying the knot",
            "Creating the starting stitch to anchor the seam",
            "Stitching backward into the previous hole to form a continuous line",
            "Securing the seam with a final knot"
        ],
        "answer": 1,
        "images": ["3.1.png"],
        "explanation": {
            "correct":   "This image shows the first stitch— threading the needle to the back on the right and bringing the needle to the front with an equal distance.",
            "incorrect": "Not quite—the image shows the first initial anchoring stitch, not the final knot or the backward stitching."
        },
        "explanation_images": []
    },
    "4": {
        "text": "Why is slip stitch preferred over backstitch?",
        "choices": [
            "It uses thicker thread",
            "It has overlapping stitches that form a solid line",
            "It’s nearly invisible from the outside",
            "It uses double the fabric"
        ],
        "answer": 2,
        "images": [],
        "explanation": {
            "correct":   "Exactly—slip stitch hides the thread almost entirely, making the hem nearly invisible.",
            "incorrect": "The correct answer is: It’s nearly invisible from the outside. The stitches on the top are only a few threads wide."
        },
        "explanation_images": ["4.1.png"]
    },
    "5": {
        "text": "Click where to insert the needle next for slip stitch.",
        "choices": ["1", "2", "3"],
        "answer": 2, # index of the hotspot
        "images": ["5.1.png"],  
        "hotspots": [
            { "top": "50%", "left": "25%" },   # spot 0
            { "top": "25%", "left": "40%" },   # spot 1
            { "top": "55%", "left": "47%" }    # spot 2
        ],
        "explanation": {
            "correct":   "It goes on top very close to the current stitch.",
            "incorrect": "Actually you should insert at spot 3, close to the current stitch."
        },
        "explanation_images": []
    },
    "6": {
        "text": "Click where to insert the needle next for backstitch after pulling the needle through.",
        "choices": ["1", "2", "3"],
        "answer": 0, # index of the hotspot
        "images": ["6.1.png"],
        "hotspots": [
            { "top": "45%", "left": "35%" },   # spot 1
            { "top": "45%", "left": "60%" },   # spot 2
            { "top": "45%", "left": "75%" }    # spot 3
        ],
        "explanation": {
            "correct":   "It goes back to the entry of the previous stitch.",
            "incorrect": "After pulling through you return to spot 2, the entry of the previous stitch."
        },
        "explanation_images": []
    }
}


quiz_responses = []

def log_page_entry(page_name):
    with open("page_enter_log.txt", "a") as f:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        ip = request.remote_addr or "unknown"
        f.write(f"{timestamp} - {ip} - {page_name}\n")



@app.route('/')
def home():
   return render_template('home.html')   


@app.route('/hem')
def hem_index():
    return redirect(url_for('hem_step', step=0))

@app.route('/hem/<int:step>')
def hem_step(step):
    log_page_entry(f"hem/{step}")
    return render_template("hem.html", step=hem_steps[step], step_num=step,
                           prev_step=step - 1 if step > 0 else None,
                           next_step=step + 1 if step < len(hem_steps) - 1 else None)


@app.route('/backstitch')
def backstitch_index():
    return redirect(url_for('backstitch_step', step=0))

@app.route('/backstitch/<int:step>')
def backstitch_step(step):
    log_page_entry(f"backstitch/{step}")
    return render_template("backstitch.html", step=backstitch_steps[step],
                           prev_step=step - 1 if step > 0 else None,
                           next_step=step + 1 if step < len(backstitch_steps) - 1 else None)

@app.route('/slipstitch')
def slipstitch_index():
    return redirect(url_for('slipstitch_step', step=0))

@app.route('/slipstitch/<int:step>')
def slipstitch_step(step):  
    log_page_entry(f"slipstitch/{step}")
    return render_template("slipstitch.html", step=slipstitch_steps[step],
                           prev_step=step - 1 if step > 0 else None,
                           next_step=step + 1 if step < len(slipstitch_steps) - 1 else None)



# … all your imports, hem_steps, backstitch_steps, slipstitch_steps, quiz_questions, quiz_responses …

@app.route('/quiz', defaults={'qid': None}, methods=['GET','POST'], endpoint='quiz')
@app.route('/quiz/<int:qid>',            methods=['GET','POST'])
def quiz(qid):
    total = len(quiz_questions)

    # ---- 1) entry point: /quiz  ----
    if qid is None:
        quiz_responses.clear()
        return redirect(url_for('quiz', qid=1))

    # ---- 2) out of range → restart ----
    if qid < 1 or qid > total:
        return redirect(url_for('quiz', qid=1))

    # grab question
    q = quiz_questions[str(qid)]

    # ---- 3) on submit, render feedback  ----
    if request.method == 'POST':
        sel     = int(request.form['choice'])
        correct = (sel == q['answer'])
        quiz_responses.append({ 'qid': qid, 'selected': sel, 'correct': correct })

        feedback = q['explanation']['correct'] if correct else q['explanation']['incorrect']
        next_qid = qid + 1 if qid < total else None

        return render_template(
            'quiz.html',
            qid=qid,
            total=total,
            question=q['text'],
            choices=q['choices'],
            show_feedback=True,
            correct=correct,
            feedback=feedback,
            images=q['images'],
            explanation_images=q.get('explanation_images', []),
            hotspots=q.get('hotspots', []),
            next_qid=next_qid,
            selected=sel,
            answer=q['answer']
        )

    # ---- 4) initial GET: render question form  ----
    return render_template(
        'quiz.html',
        qid=qid,
        total=total,
        question=q['text'],
        choices=q['choices'],
        show_feedback=False,
        images=q['images'],
        hotspots=q.get('hotspots', []),
        answer=q['answer']
    )



@app.route('/quiz/result')
def quiz_result():
    total = len(quiz_questions)
    score = sum(1 for r in quiz_responses if r['correct'])
    return render_template(
      'quiz_result.html',
      score=score,
      total=total
    )



if __name__ == '__main__':
   app.run(debug = True, port=5001)