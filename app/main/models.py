from app import db # we already defined db instance inside app/__init__.py file
import datetime
# from app.auth.models import User

class TASK(db.Model):
    __tablename__ = 'TASK'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    context = db.Column(db.String(500), nullable = False)
    complexity = db.Column(db.String(500), nullable = False)
    quality = db.Column(db.String(500), nullable = False)
    delay = db.Column(db.String(500), nullable = False)
    filler_type = db.Column(db.String(500), nullable = False)
    URL_completion_code = db.Column(db.String(500))
    time_stamp = db.Column(db.DateTime, default = datetime.datetime.utcnow())

    def __init__(self, title, context, complexity, quality, delay, filler_type, URL_completion_code):
        self.title = title
        self.context = context
        self.complexity = complexity
        self.quality = quality
        self.delay = delay
        self.filler_type = filler_type
        self.URL_completion_code = URL_completion_code

class WORKER(db.Model):
    __tablename__ = 'WORKER'
    id = db.Column(db.Integer, primary_key = True)
    prolific_id = db.Column(db.String(100))
    time_stamp = db.Column(db.DateTime, default = datetime.datetime.utcnow())

    def __init__(self, prolific_id):
        self.prolific_id = prolific_id

class SURVEY(db.Model):

    __tablename__ = 'SURVEY'
    id = db.Column(db.Integer, primary_key = True)
    w_id = db.Column(db.Integer, db.ForeignKey('WORKER.id'))
    t_id = db.Column(db.Integer, db.ForeignKey('TASK.id'))
    #survey items

    mood = db.Column(db.String(500), nullable = False)

    #------------------time perception---------------------------------
    PWT = db.Column(db.String(500), nullable = False)
    cognitive = db.Column(db.String(500), nullable = False)

    #------------------emotional experience-----------------------------
    affective_irritation = db.Column(db.String(500), nullable = False)
    affective_fairness = db.Column(db.String(500), nullable = False)
    affective_annoyance = db.Column(db.String(500), nullable = False)
    affective_boredom = db.Column(db.String(500), nullable = False)
    affective_stress = db.Column(db.String(500), nullable = False)

    #cognitive absorption
    #---------------------focused immersion-------------------------------
    FI1 = db.Column(db.String(500), nullable = False)
    FI2 = db.Column(db.String(500), nullable = False)
    FI3 = db.Column(db.String(500), nullable = False)
    FI4 = db.Column(db.String(500), nullable = False)

    #---------------------Temporal Dissociation----------------------------
    TD1 = db.Column(db.String(500), nullable = False)
    TD2 = db.Column(db.String(500), nullable = False)
    TD3 = db.Column(db.String(500), nullable = False)
    TD4 = db.Column(db.String(500), nullable = False)
    TD5 = db.Column(db.String(500), nullable = False)

    #---------------------Heightened Enjoyment-----------------------------
    HE1 = db.Column(db.String(500), nullable = False)
    HE2 = db.Column(db.String(500), nullable = False)
    HE3 = db.Column(db.String(500), nullable = False)
    HE4 = db.Column(db.String(500), nullable = False)

    #---------------------control------------------------------------------
    CO1 = db.Column(db.String(500), nullable = False)
    CO2 = db.Column(db.String(500), nullable = False)
    CO3 = db.Column(db.String(500), nullable = False)


    #---------------------Curiosity----------------------------------------
    CU1 = db.Column(db.String(500), nullable = False)
    CU2 = db.Column(db.String(500), nullable = False)
    CU3 = db.Column(db.String(500), nullable = False)


    #---------------------Perceived uncertainty-----------------------------
    PU1 = db.Column(db.String(500), nullable = False)
    PU2 = db.Column(db.String(500), nullable = False)
    PU3 = db.Column(db.String(500), nullable = False)
    PU4 = db.Column(db.String(500), nullable = False)


    #---------------------UEQ----------------------------------------------
    UEQ1 = db.Column(db.String(500), nullable = False)
    UEQ2 = db.Column(db.String(500), nullable = False)
    UEQ3 = db.Column(db.String(500), nullable = False)
    UEQ4 = db.Column(db.String(500), nullable = False)
    UEQ5 = db.Column(db.String(500), nullable = False)
    UEQ6 = db.Column(db.String(500), nullable = False)
    UEQ7 = db.Column(db.String(500), nullable = False)
    UEQ8 = db.Column(db.String(500), nullable = False)

    satisfaction  = db.Column(db.String(500), nullable = False)


    social_o_1  = db.Column(db.String(500), nullable = False)
    social_o_2  = db.Column(db.String(500), nullable = False)

    exp1  = db.Column(db.String(500), nullable = False)
    exp2  = db.Column(db.String(500), nullable = False)

    feedback  = db.Column(db.String(500), nullable = False)
    education = db.Column(db.String(500), nullable = False)

    time_stamp = db.Column(db.DateTime, default = datetime.datetime.utcnow)

    def __init__(self, w_id, t_id, mood, PWT, cognitive, affective_irritation, affective_fairness, \
    affective_annoyance, affective_boredom, affective_stress, FI1, FI2, FI3, FI4, TD1, TD2, TD3, TD4, TD5, \
    HE1, HE2, HE3, HE4, CO1, CO2, CO3, CU1, CU2, CU3, PU1, PU2, PU3, PU4, UEQ1, UEQ2, UEQ3, UEQ4, UEQ5, UEQ6, UEQ7, UEQ8, satisfaction, \
    feedback, exp1, exp2, social_o_1, social_o_2, education):
        self.w_id = w_id
        self.t_id = t_id
        self.mood = mood
        self.PWT = PWT
        self.cognitive = cognitive
        self.affective_irritation = affective_irritation
        self.affective_fairness = affective_fairness
        self.affective_annoyance = affective_annoyance
        self.affective_boredom = affective_boredom
        self.affective_stress = affective_stress
        #Focued immersion
        self.FI1 = FI1
        self.FI2 = FI2
        self.FI3 = FI3
        self.FI4 = FI4
        #Tempral Dissociation
        self.TD1 = TD1
        self.TD2 = TD2
        self.TD3 = TD3
        self.TD4 = TD4
        self.TD5 = TD5
        # Heightened Enjoyment
        self.HE1 = HE1
        self.HE2 = HE2
        self.HE3 = HE3
        self.HE4 = HE4
        #control
        self.CO1 = CO1
        self.CO2 = CO2
        self.CO3 = CO3

        #curiousity
        self.CU1 = CU1
        self.CU2 = CU2
        self.CU3 = CU3

        #perceived uncertainty
        self.PU1 = PU1
        self.PU2 = PU2
        self.PU3 = PU3
        self.PU4 = PU4

        #UEQ
        self.UEQ1 = UEQ1
        self.UEQ2 = UEQ2
        self.UEQ3 = UEQ3
        self.UEQ4 = UEQ4
        self.UEQ5 = UEQ5
        self.UEQ6 = UEQ6
        self.UEQ7 = UEQ7
        self.UEQ8 = UEQ8

        self.satisfaction = satisfaction

        self.feedback = feedback

        self.social_o_1 = social_o_1
        self.social_o_2 = social_o_2

        self.exp1 = exp1
        self.exp2 = exp2

        self.education = education

class MESSAGE(db.Model):

    __tablename__ = 'MESSAGE'
    id = db.Column(db.Integer, primary_key = True)
    w_id = db.Column(db.Integer, db.ForeignKey('WORKER.id'))
    t_id = db.Column(db.Integer, db.ForeignKey('TASK.id'))
    question = db.Column(db.String(1000), nullable = False)
    user_utterance = db.Column(db.String(500), nullable = False)
    start_time = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    end_time =db.Column(db.DateTime)

    def __init__(self, question, user_utterance, w_id, t_id, start_time, end_time):
        self.question = question
        self.user_utterance = user_utterance
        self.w_id = w_id
        self.t_id = t_id
        self.end_time = end_time
        self.start_time = start_time

class TIME_SPENT(db.Model):
    __tablename__ = 'TIME_SPENT'
    id = db.Column(db.Integer, primary_key = True)
    w_id = db.Column(db.Integer, db.ForeignKey('WORKER.id'))
    t_id = db.Column(db.Integer, db.ForeignKey('TASK.id'))

    stage = db.Column(db.String(500), nullable = False)
    start_time = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    end_time =db.Column(db.DateTime)

    def __init__(self, stage, w_id, t_id, start_time, end_time):
        self.stage = stage
        self.w_id = w_id
        self.t_id = t_id
        self.end_time = end_time
        self.start_time = start_time
