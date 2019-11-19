from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField, SelectField
from wtforms.validators import DataRequired

class RegisterFormToukou(FlaskForm):
   
    
    fnameJp     = StringField("名前", validators=[DataRequired()])
    lnameJp     = StringField("苗字", validators=[DataRequired()])
    fnameEn     = StringField("名前（英語）", validators=[DataRequired()])
    lnameEn     = StringField("苗字（英語）", validators=[DataRequired()])
    username    = StringField("ユーザーネーム", validators=[DataRequired()])
    email       = StringField("Eメール", validators=[DataRequired()])
    password    = PasswordField("パスワード", validators=[DataRequired()])
    c_password  = PasswordField("パスワード", validators=[DataRequired()])
    statusNow   = SelectField("ステータス", 
        choices=[('daigaku', '大学生'), ('komikare', 'コミカレ生'), ('gogaku', '語学学生'), ('alumni', '社会人')]
    )
    university  = SelectField("ステータス",
        choices=[('ucla', 'UCLA'), ('uci', 'UCI'), ('ucb', 'UC Berkeley')]
    )
    majorType   = SelectField("分野", 
        choices=[('bunkei','文系'),('rikei','理系'),('both','文系と理系'),('other','他')]
    )
    country     = SelectField("国",
        choices=[('usa', 'アメリカ')]
    )
    submit      = SubmitField("登録する")

    def validate_email(form, field):
        banned = ['gmail', 'hotmail', 'yahoo', 'icloud', 'aol' ]
        if banned in text:
            return ValidationError("大学のEメールを使ってください")

class LoginFormToukou(FlaskForm):
    username    = StringField("ユーザーネーム", validators=[DataRequired()])
    password    = PasswordField("パスワード", validators=[DataRequired()])
    submit      = SubmitField("ログイン")

#class RegisterFormIppan(FlaskForm):
    #--