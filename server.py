<<<<<<< HEAD
from flask import Flask,render_template,request,redirect,url_for,jsonify
from db_conetion import *
from collections import OrderedDict


app=Flask(__name__)




@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/producteur",methods=['POST','GET'])
def producteur():
    if request.method=='POST':
        username=request.form["username"]
        tel=request.form["tel"]
        collecteur=request.form["collecteur"]
        Producteur.create(username=username, tel=tel, collecteur=collecteur)
        print("created!:!!")
    else:
        print("no get requested")
    return render_template("producteur.html")

@app.route("/list_producteurs")
def list_producteurs():
    producteurs=Producteur.select().order_by(Producteur.username.desc())
    return render_template("list_producteurs.html",lst=producteurs)


@app.route("/delete_producteur",methods=['POST','GET'])
def delete_producteur():
    #Producteur.delete()
    if request.method=="GET":
        ids=request.args['key']
        producteur=Producteur.get(Producteur.id==ids)
        producteur.delete_instance()
        
    return redirect(url_for("list_producteurs"))
    
@app.route("/list_moves",methods=['POST','GET'])
def list_moves():
    if request.method=="GET" and request.args.get('key'):
        ids=request.args.get('key')
        producteur=Producteur.get(Producteur.id==ids)
        moves=Moves.select().where(Moves.producteur==producteur).order_by(Moves.moves_date.desc())    
    else:
        moves=Moves.select().order_by(Moves.moves_date.desc())
    return render_template("list_moves.html",lst=moves)


@app.route("/moves",methods=["POST","GET"])
def moves():
    producteurs=Producteur.select().order_by(Producteur.username.desc())
    if request.method=="POST":
        user_id=request.form.get("user_id")
        qtt=request.form.get("qtt")
        note=request.form.get("note")
        moves_date=request.form.get("moves_date")
        moves_type=request.form.get("moves_type")
        if moves_date=="":
            Moves.create(producteur=user_id, qtt=qtt,note=note,moves_type=moves_type)
        else:    
            Moves.create(producteur=user_id, qtt=qtt,note=note,moves_type=moves_type,moves_date=moves_date)
        print("*"+moves_date+"*")
    return render_template("moves.html",lst=producteurs)
    


@app.route("/delete_moves",methods=['POST','GET'])
def delete_moves():
    #Producteur.delete()
    if request.method=="GET":
        ids=request.args['key']
        move=Moves.get(Moves.id==ids)
        move.delete_instance()
        
    return redirect(url_for("list_moves"))



def query(myvar):
    return Moves.select(Moves.producteur,Moves.moves_date,Moves.note,fn.sum(Moves.qtt).alias("sum_qtt"),Moves.moves_type).group_by(myvar)

@app.route("/moves_report")
def moves_report():
    moves=None
    group_by="all"
    if request.method=="GET":
        group_by=request.args.get("group_by")
        print(group_by)
        if group_by=="aliment":
            moves=Moves.select(fn.sum(Moves.qtt).alias("sum_qtt"),Moves.moves_type).group_by(Moves.moves_type)
        else:
            if group_by=="producteur":
                moves=Moves.select(Moves.producteur,fn.sum(Moves.qtt).alias("sum_qtt")).group_by(Moves.producteur)
            else:
                if group_by=="all":
                    moves=Moves.select().order_by(Moves.producteur)
                else:
                    if group_by=="qtt":
                        moves=Moves.select(Moves.qtt,fn.count(Moves.qtt).alias("qtt_count")).group_by(Moves.qtt)
            
        
    return render_template("moves_report.html",lst=moves,group_by=group_by)

@app.route('/report')
def report():
    producteurs=Producteur.select()
    return jsonify({"user":"helbouti"})

if __name__ == "__main__":
    initialize()
=======
from flask import Flask,render_template,request,redirect,url_for
from db_conetion import *
from collections import OrderedDict


app=Flask(__name__)




@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/producteur",methods=['POST','GET'])
def producteur():
    if request.method=='POST':
        username=request.form["username"]
        tel=request.form["tel"]
        collecteur=request.form["collecteur"]
        Producteur.create(username=username, tel=tel, collecteur=collecteur)
        print("created!:!!")
    else:
        print("no get requested")
    return render_template("producteur.html")

@app.route("/list_producteurs")
def list_producteurs():
    producteurs=Producteur.select().order_by(Producteur.username.desc())
    return render_template("list_producteurs.html",lst=producteurs)


@app.route("/delete_producteur",methods=['POST','GET'])
def delete_producteur():
    #Producteur.delete()
    if request.method=="GET":
        ids=request.args['key']
        producteur=Producteur.get(Producteur.id==ids)
        producteur.delete_instance()
        
    return redirect(url_for("list_producteurs"))
    
@app.route("/list_moves",methods=['POST','GET'])
def list_moves():
    if request.method=="GET" and request.args.get('key'):
        ids=request.args.get('key')
        producteur=Producteur.get(Producteur.id==ids)
        moves=Moves.select().where(Moves.producteur==producteur).order_by(Moves.moves_date.desc())    
    else:
        moves=Moves.select().order_by(Moves.moves_date.desc())
    return render_template("list_moves.html",lst=moves)


@app.route("/moves",methods=["POST","GET"])
def moves():
    producteurs=Producteur.select().order_by(Producteur.username.desc())
    if request.method=="POST":
        user_id=request.form.get("user_id")
        qtt=request.form.get("qtt")
        note=request.form.get("note")
        moves_date=request.form.get("moves_date")
        moves_type=request.form.get("moves_type")
        if moves_date=="":
            Moves.create(producteur=user_id, qtt=qtt,note=note,moves_type=moves_type)
        else:    
            Moves.create(producteur=user_id, qtt=qtt,note=note,moves_type=moves_type,moves_date=moves_date)
        print("*"+moves_date+"*")
    return render_template("moves.html",lst=producteurs)
    


@app.route("/delete_moves",methods=['POST','GET'])
def delete_moves():
    #Producteur.delete()
    if request.method=="GET":
        ids=request.args['key']
        move=Moves.get(Moves.id==ids)
        move.delete_instance()
        
    return redirect(url_for("list_moves"))



def query(myvar):
    return Moves.select(Moves.producteur,Moves.moves_date,Moves.note,fn.sum(Moves.qtt).alias("sum_qtt"),Moves.moves_type).group_by(myvar)

@app.route("/moves_report")
def moves_report():
    moves=None
    group_by="all"
    if request.method=="GET":
        group_by=request.args.get("group_by")
        print(group_by)
        if group_by=="aliment":
            moves=Moves.select(fn.sum(Moves.qtt).alias("sum_qtt"),Moves.moves_type).group_by(Moves.moves_type)
        else:
            if group_by=="producteur":
                moves=Moves.select(Moves.producteur,fn.sum(Moves.qtt).alias("sum_qtt")).group_by(Moves.producteur)
            else:
                if group_by=="all":
                    moves=Moves.select().order_by(Moves.producteur)
                else:
                    if group_by=="qtt":
                        moves=Moves.select(Moves.qtt,fn.count(Moves.qtt).alias("qtt_count")).group_by(Moves.qtt)
            
        
    return render_template("moves_report.html",lst=moves,group_by=group_by)



if __name__ == "__main__":
    initialize()
>>>>>>> 064a1ad8fc32c26ea00738208d144939b52c8acd
    app.run(debug=True)