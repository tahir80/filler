from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, FloatField, SelectField, TextAreaField, RadioField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, NumberRange, InputRequired

dropdown_list = [(1,'1'),(2,'1')]
class CreateNewProject(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    context = RadioField('Select the context of this task',
                   choices=[('stress','stress'),('IR','IR')])
    # context = StringField('context', validators=[DataRequired()])
    complexity = RadioField('Select the complexity level',
                   choices=[('1','high'),('0','low')])
    quality = RadioField('Select the quality level',
                       choices=[('1','high'),('0','low')])

    delay = RadioField('Select the delay level',
                       choices=[('8','8-sec'),('16','16-sec'),('32','32-sec')])

    filler = RadioField('Select the filler type',
                       choices=[('CF','CF'),('nature','nature'),('manmade','manmade'),('micro','micro'), ('box','box'), ('dots','dots'), ('progress','progress'), ('no-filler','no-filler')])

    URL_completion_code = StringField('URL Completion Code', validators=[InputRequired()])
    # quality = FloatField('quality', validators=[DataRequired()])
    # delay = StringField('delay', validators=[DataRequired()])
    submit = SubmitField("create a new task")
    # deactivate = SubmitField('DEACTIVATE THIS TASK')

class EditProject(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    context = RadioField('Select the context of this task',
                   choices=[('stress','stress'),('IR','IR')])
    # context = StringField('context', validators=[DataRequired()])
    complexity = RadioField('Select the complexity level',
                   choices=[('1','high'),('0','low')])
    quality = RadioField('Select the quality level',
                       choices=[('1','high'),('0','low')])

    delay = RadioField('Select the delay level',
                      choices=[('8','8-sec'),('16','16-sec'),('32','32-sec')])

    filler = RadioField('Select the filler type',
                        choices=[('CF','CF'),('nature','nature'),('manmade','manmade'),('micro','micro'), ('box','box'), ('dots','dots'), ('progress','progress'), ('no-filler','no-filler')])

    url = StringField('URL Completion Code', validators=[InputRequired()])
    # quality = FloatField('quality', validators=[DataRequired()])
    # delay = StringField('delay', validators=[DataRequired()])
    submit = SubmitField("Update")


class surveys(FlaskForm):
    Perceived_waiting_time = IntegerField('How did you perceive the response time from ___ to be during your conversation? Indicate your estimate in seconds by simply entering the number of seconds. ',
                                        validators=[InputRequired(), NumberRange(min=1, max=600)])

    cognitive = RadioField('How would you best describe the response time from ___ during your conversation? ',
               choices=[('1','Very  Short'),('2','Short'), ('3','Normal'),('4','Long'), ('5', 'Very long')])

    irritation  = RadioField('Irritation',
                  choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5')])

    fairness  = RadioField('Unfairness',
                      choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5')])

    annoyance  = RadioField('Annoyance',
                choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5')])

    boredom  = RadioField('Boredom',
                    choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5')])

    stress  = RadioField('Stress',
                    choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5')])

    # attitude  = RadioField('Please indicate your attitude towards the response time of ___.',
    #                choices=[('1','Intolerable delay'),('2','Excessive but still tolerable delay'), ('3','Acceptable delay'),('4','Not significant delay')])

    satisfaction  = RadioField('Indicate your overall satisfaction with the service provided by CPCS',
                   choices=[('1','1'),('2','2'), ('3','3'),('4','4'),('5','5'),('6','6'), ('7','7'),('8','8'), ('9','9'), ('10','10')])

    feedback     = TextAreaField('Please share any additional thoughts, remarks, or feedback that you may have regarding your experience interacting with ___.', validators=[InputRequired()])

    # suggestion     = TextAreaField('Do you have any suggestions for how conversational systems can handle long delays in responses? Please share your thoughts on this.')


    social_o_1 =  RadioField("I think 'small talk' with a chatbot is enjoyable ",
                   choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    social_o_2 =  RadioField("I like chatting casually with a chatbot",
                   choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])


    exp1 =  RadioField("I am familiar with chatbot technologies ",
                   choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    exp2 =  RadioField("I use chatbots frequently. ",
                   choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])


    education = SelectField('What’s your highest level of education?', [DataRequired()],
        choices=[
            ("", "---"),
            ('No formal education', ' No formal education'),
            ('High school diploma', 'High school diploma'),
            ('College degree', 'College degree'),
            ('Vocational training', 'Vocational training'),
            ('Bachelor’s degree', 'Bachelor’s degree'),
            ('Master’s degree', 'Master’s degree'),
            ('Professional degree', 'Professional degree'),
            ('Doctorate degree', 'Doctorate degree'),
            ('Other', 'Other'),
        ]
    )
    #-----------------------------------------------------------------------------------------------------------
    #Focused Immersion
    FI1 =  RadioField("I was intensely absorbed in a filler while waiting to see the results.",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    FI2 =  RadioField("My attention was focused on a filler while I was waiting to see the results.",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    FI3 =  RadioField("I concentrated fully on a filler while waiting to see the results.",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    FI4 =  RadioField("I was deeply immersed in a filler while waiting to see the results.",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    #------------------------------------------------------------------------------------------------------------
    # Temporal Dissociation
    TD1 =  RadioField("Time appeared to go by very quickly while waiting to see the results.",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    TD2 =  RadioField("I lost track of time while waiting to see the results.",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    TD3 =  RadioField("I was unconscious of the passage of time while waiting to see the results.",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    TD4 =  RadioField("Time seemed to fly while I was waiting to see the results.",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    TD5 =  RadioField("While waiting to see the results, I forgot the passage of time.",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    #--------------------------------------------------------------------------------------------------------------
    #Heightened Enjoyment
    HE1 =  RadioField("Waiting for the requested results in the filler was pleasant",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    HE2 =  RadioField("Waiting for the requested results in the filler was enjoyable",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    HE3 =  RadioField("Waiting for the requested results in the filler was fun",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    HE4 =  RadioField("Waiting for the requested results in the filler was exciting",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])


    #----------------------------------------------------------------------------------------------------------------
    #control
    CO1 =  RadioField("When using CPCS I feel in control",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    CO2 =  RadioField("I feel that I have no control over my interaction with CPCS",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    CO3 =  RadioField("CPCS allows me to control my interaction",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])


    #-------------------------------------------------------------------------------------------------------------
    #Curiosity
    CU1 =  RadioField("Using CPCS excites my curiosity",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    CU2 =  RadioField("Interacting with CPCS makes me curious",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    CU3 =  RadioField("Using CPCS arouses my imagination",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])


    #----------------------------------------------------------------------------------------------------------------
    # Perceived uncertainty
    PU1 =  RadioField("I was uneasy while I was waiting for the requested results.",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    PU2 =  RadioField("I was anxious while I was waiting for the requested results.",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    PU3 =  RadioField("I was uncertain while I was waiting for the requested results.",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])

    PU4 =  RadioField("I was unsettled while I was waiting for the requested results.",
                       choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5'), ('6', '6'),('7', '7')])


   #----------------------------------------------------------------------------------------------------------------
   # UEQ
    UEQ1 =  RadioField("",
                      choices=[('-3','-3'),('-2','-2'), ('-1','-1'),('0','0'), ('1', '1'), ('2', '2'),('3', '3')])

    UEQ2 =  RadioField("",
                      choices=[('-3','-3'),('-2','-2'), ('-1','-1'),('0','0'), ('1', '1'), ('2', '2'),('3', '3')])

    UEQ3 =  RadioField("",
                      choices=[('-3','-3'),('-2','-2'), ('-1','-1'),('0','0'), ('1', '1'), ('2', '2'),('3', '3')])

    UEQ4 =  RadioField("",
                      choices=[('-3','-3'),('-2','-2'), ('-1','-1'),('0','0'), ('1', '1'), ('2', '2'),('3', '3')])

    UEQ5 =  RadioField("",
                      choices=[('-3','-3'),('-2','-2'), ('-1','-1'),('0','0'), ('1', '1'), ('2', '2'),('3', '3')])

    UEQ6 =  RadioField("",
                      choices=[('-3','-3'),('-2','-2'), ('-1','-1'),('0','0'), ('1', '1'), ('2', '2'),('3', '3')])

    UEQ7 =  RadioField("",
                      choices=[('-3','-3'),('-2','-2'), ('-1','-1'),('0','0'), ('1', '1'), ('2', '2'),('3', '3')])

    UEQ8 =  RadioField("",
                      choices=[('-3','-3'),('-2','-2'), ('-1','-1'),('0','0'), ('1', '1'), ('2', '2'),('3', '3')])



    submit = SubmitField('Submit')
