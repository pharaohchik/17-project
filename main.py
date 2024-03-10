from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def posts():
    post = [
        {
            'name_author': 'maksimka',
            'text': 'Maximka is next to a cool rhinoceros.',
            'image': 'maksimka.jpg',
            'amount_likes': 999
        },
        {
            'name_author': 'karapusik',
            'text': 'тимоша устал',
            'image': 'karapus.jpg',
            'amount_likes': 250
        },
        {
            'name_author': 'tamara lox',
            'text': 'очень пафосная тамара',
            'image': 'tamara.jpg',
            'amount_likes': 2999
        },
        {
            'name_author': 'vanechka popov',
            'text': 'очень крутой некий ванек',
            'image': 'vanya.jpg',
            'amount_likes': 378
        }
    ]
    return render_template('page_vk.html', posts=post)


if __name__ == '__main__':
    app.run()
#000