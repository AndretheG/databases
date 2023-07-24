"""Forms for playlist app."""

from wtforms import SelectField, StringField, validators, TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import Optional


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    
    name = StringField("Name", validators=[validators.DataRequired()])
    description = TextAreaField("Description", valdidators=[Optional()])



class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField('Title', validators=[validators.DataRequired()])
    artist = StringField('Artist', validators=[validators.DataRequired()])

   


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
