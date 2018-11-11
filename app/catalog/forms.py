from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, FloatField
from wtforms.validators import DataRequired


class EditBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    format = StringField('Format', validators=[DataRequired()])
    num_pages = StringField('Pages', validators=[DataRequired()])
    author = StringField('Author',validators=[DataRequired()])
    avg_rating = FloatField('Average rating',validators=[DataRequired()])
    submit = SubmitField('Update')


class CreateBookForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    author = StringField('Author',validators=[DataRequired()])
    avg_rating = FloatField('Average Rating',validators=[(DataRequired())])
    book_format = StringField('Format',validators=[DataRequired()])
    img_url =  StringField('Image',validators=[DataRequired()])
    pub_id = IntegerField('PublisherId',validators=[DataRequired()])
    num_pages = IntegerField('Number Of Pages',validators=[DataRequired()])
    submit = SubmitField('Create')