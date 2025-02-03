# app.py
from flask import Flask, render_template, redirect, url_for, request, flash, session
from config import Config
from models import db, User, Project, Group

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


def create_tables_and_default_user():
    """Erstellt die Tabellen und legt einen Standardbenutzer an."""
    db.create_all()
    # Standardbenutzer anlegen, falls nicht vorhanden
    if not db.session.query(User).filter_by(username='admin').first():
        admin = User(username='admin')
        admin.set_password('adminpass')  # Standardpasswort – bitte in der Produktion ändern!
        db.session.add(admin)
        db.session.commit()


### Login und Dashboard ###

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = db.session.query(User).filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            flash('Login erfolgreich!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Ungültige Anmeldedaten', 'danger')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Erfolgreich ausgeloggt!', 'info')
    return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Bitte logge dich zuerst ein.', 'warning')
        return redirect(url_for('login'))
    user = db.session.get(User, session['user_id'])
    return render_template('dashboard.html', user=user)


### Benutzerverwaltung ###

@app.route('/users')
def user_list():
    if 'user_id' not in session:
        flash('Bitte logge dich zuerst ein.', 'warning')
        return redirect(url_for('login'))
    users = db.session.query(User).all()
    return render_template('user_list.html', users=users)


@app.route('/users/create', methods=['GET', 'POST'])
def user_create():
    if 'user_id' not in session:
        flash('Bitte logge dich zuerst ein.', 'warning')
        return redirect(url_for('login'))
    groups = db.session.query(Group).all()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        group_ids = request.form.getlist('groups')
        if db.session.query(User).filter_by(username=username).first():
            flash('Benutzername existiert bereits!', 'danger')
        else:
            new_user = User(username=username)
            new_user.set_password(password)
            for gid in group_ids:
                grp = db.session.get(Group, int(gid))
                if grp:
                    new_user.groups.append(grp)
            db.session.add(new_user)
            db.session.commit()
            flash('Benutzer erfolgreich erstellt!', 'success')
            return redirect(url_for('user_list'))
    return render_template('user_form.html', action='Erstellen', user=None, groups=groups)


@app.route('/users/edit/<int:user_id>', methods=['GET', 'POST'])
def user_edit(user_id):
    if 'user_id' not in session:
        flash('Bitte logge dich zuerst ein.', 'warning')
        return redirect(url_for('login'))
    user = db.session.get(User, user_id)
    if not user:
        flash('Benutzer nicht gefunden!', 'danger')
        return redirect(url_for('user_list'))
    groups = db.session.query(Group).all()
    if request.method == 'POST':
        user.username = request.form.get('username')
        password = request.form.get('password')
        if password:
            user.set_password(password)
        # Gruppen zuweisen
        group_ids = request.form.getlist('groups')
        user.groups = []  # bestehende Gruppen leeren
        for gid in group_ids:
            grp = db.session.get(Group, int(gid))
            if grp:
                user.groups.append(grp)
        db.session.commit()
        flash('Benutzer erfolgreich aktualisiert!', 'success')
        return redirect(url_for('user_list'))
    return render_template('user_form.html', action='Bearbeiten', user=user, groups=groups)


### Projektverwaltung ###

@app.route('/projects')
def project_list():
    if 'user_id' not in session:
        flash('Bitte logge dich zuerst ein.', 'warning')
        return redirect(url_for('login'))
    projects = db.session.query(Project).all()
    return render_template('project_list.html', projects=projects)


@app.route('/projects/create', methods=['GET', 'POST'])
def project_create():
    if 'user_id' not in session:
        flash('Bitte logge dich zuerst ein.', 'warning')
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        # Hier wird der aktuell angemeldete Benutzer als Manager gesetzt.
        project = Project(name=name, description=description, manager_id=session['user_id'])
        db.session.add(project)
        db.session.commit()
        flash('Projekt erfolgreich erstellt!', 'success')
        return redirect(url_for('project_list'))
    return render_template('project_form.html', action='Erstellen', project=None)


### Gruppenverwaltung ###

@app.route('/groups')
def group_list():
    if 'user_id' not in session:
        flash('Bitte logge dich zuerst ein.', 'warning')
        return redirect(url_for('login'))
    groups = db.session.query(Group).all()
    return render_template('group_list.html', groups=groups)


@app.route('/groups/create', methods=['GET', 'POST'])
def group_create():
    if 'user_id' not in session:
        flash('Bitte logge dich zuerst ein.', 'warning')
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form.get('name')
        if db.session.query(Group).filter_by(name=name).first():
            flash('Gruppe existiert bereits!', 'danger')
        else:
            group = Group(name=name)
            db.session.add(group)
            db.session.commit()
            flash('Gruppe erfolgreich erstellt!', 'success')
            return redirect(url_for('group_list'))
    return render_template('group_form.html', action='Erstellen', group=None)


if __name__ == '__main__':
    with app.app_context():
        create_tables_and_default_user()
    app.run(debug=True)
