# -------------------------------------------------------------

from flask import (
    abort,
    Blueprint, 
    flash,
    redirect,
    render_template,
    request, 
    url_for,
)

from app.forms.natural_person_form import NaturalPersonForm
from app.forms.natural_person_search_form import NaturalPersonSearchForm
from app.dtos.natural_person_dto import NaturalPersonDTO
from app.services.login_service import LoginService
from app.services.natural_person_service import NaturalPersonService
from app.utils.formats import Format

# -------------------------------------------------------------

natural_person_bp = Blueprint("natural_person_routes", __name__)
natural_person_service = NaturalPersonService()
login_service = LoginService()
login_required = login_service.login_required
format = Format()

# -------------------------------------------------------------

@natural_person_bp.route('/natural', methods=['POST', 'GET'])
@login_required
def natural_list():
    form = NaturalPersonSearchForm()
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    if request.method == 'POST':
        query = natural_person_service.get_natural_person_by_name(form.search.data)
    else:
        query = natural_person_service.get_all_natural_person()

    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    natural_persons = pagination.items
    return render_template(
        'person/natural/list.html',
        form=form,
        natural_persons=natural_persons,
        pagination=pagination
    )

@natural_person_bp.route('/natural/create', methods=['GET', 'POST'])
@login_required
def natural_create():
    form = NaturalPersonForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            dto = NaturalPersonDTO(form.data)
            if natural_person_service.create_natural_person(dto):
                flash('Successfully created.', 'success')
                return redirect(url_for('natural_person_routes.natural_list'))
            else:
                flash('Error creating.', 'danger')
                return redirect(url_for('natural_person_routes.natural_create'))
        return render_template('person/natural/form.html', form=form, edition=False)
    return render_template('person/natural/form.html', form=form, edition=False)


@natural_person_bp.route('/natural/details/<pk>', methods=['GET'])
@login_required
def natural_details(pk):
    person, natural_person = natural_person_service.get_natural_person_by_id(pk)
    if person and natural_person is None:
        abort(404)    
    return render_template(
        'person/natural/details.html', 
        natural_person=natural_person, 
        salary=f"R$ {format.decimal_to_maskmoney(natural_person.salary)}",
        birthday=format.birthday_format(natural_person.birthday)
    )

@natural_person_bp.route('/natural/edit/<pk>', methods=['GET', 'POST'])
@login_required
def natural_edit(pk):
    if request.method == 'POST':

        if 'delete' in request.form:
            if natural_person_service.delete_natural_person(pk):
                flash('Successfully deleted.', 'success')
                return redirect(url_for('natural_person_routes.natural_list')) 
            else:
                flash('Error deleting.', 'danger')
                return redirect(url_for('natural_person_routes.natural_list'))
            
        if 'edit' in request.form:
            person, natural_person = natural_person_service.get_natural_person_by_id(pk)
            if person is None or natural_person is None:
                abort(404)
            form = NaturalPersonForm(id=pk, data={**person.__dict__, **natural_person.__dict__})

            if form.validate_on_submit():
                dto = NaturalPersonDTO(form.data)
                print(form.data)
                if natural_person_service.edit_natural_person(pk, dto):
                    flash('Successfully edited.', 'success')
                    return redirect(url_for('natural_person_routes.natural_list'))
                else:
                    flash('Error editing.', 'danger')
                    return redirect(url_for('natural_person_routes.natural_list'))
            return render_template(
                'person/natural/form.html', 
                form=form, 
                picture=natural_person.picture, 
                edition=True
            )

    person, natural_person = natural_person_service.get_natural_person_by_id(pk)
    if person and natural_person is None:
        abort(404)
    form = NaturalPersonForm(data={**person.__dict__, **natural_person.__dict__})
    form.salary.data = format.decimal_to_maskmoney(natural_person.salary)
    return render_template(
        'person/natural/form.html', 
        form=form, 
        picture_url=natural_person.picture, 
        edition=True
    )