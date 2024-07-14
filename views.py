from django.shortcuts import render

# Create your views here.
def computer(request):
    my_dict={
        'head_msg':'Computer Department',
        'sub_msg1':'HOD : Mr. Kate Prashant D.',
        'sub_msg2':'Qualification :M.Tech (Computer Science),B.E.IT' ,
        'sub_msg3':'prashantdkate@gmail.com',
        'sub_msg4':'WELCOME TO DEPARTMENT OF COMPUTER ENGINEERING',
        'sub_msg5':'At Yashwantrao Bhonsale Institute of Technology, Sawantwadi. The department of Computer Engineering started in 2018 and has made astounding progress in the last 4 years. We have strong Diploma program in computer Engineering.The department is committed to provide quality technical computer skills in software and hardware relevant to industry. It concentrates on high academic standard backed by updated syllabus. The primary focus of the curriculum in the department is to impart technical knowledge to students, promote their problem development & solving skills and innovation of new technologies. Its enviable placement record reflects the success story of the department.',
        'sub_msg6':'The Department of Computer Engineering was started in the year 2018 with the vision to produce ethical and knowledgeable diploma holders in Computer Engineering diploma Programme. The 3 years Diploma Programme in Computer Engineering is meant for the students who have passed 10th standard. The Department has highly qualified, experienced, motivated and dedicated teaching faculty. They are actively involved in Development activities in the emerging areas of Computer Engineering. The department has well equipped 5 laboratories with 24 hours Internet facility.',
        'sub_msg7':'The aim of Computer Engineering program is to provide industry based teaching learning skills, participation in industry academic events and generating ethical and entrepreneurship skills in the students.The courses offered in this program have been designed to meet the demands of the current trend of an IT industry.',
        'sub_msg8':'"The COMPESA committee is for the students, by the students, to the students". This student association formed in the July 2019.The main motive behind forming this association is to improve the technical and non-technical skills of the students which are required beyond academics. The COMPESA committee members are elected by the students, members organizes technical and social awareness programs. Through this association our program has provided a platform for the student to develop ethical values, team management. This can be achieved by arranging various technical and non-technical events by the students. There is control of a faculty member over the association.',
    }
    return render(request,'comp.html',context=my_dict)

def electrical(request):
    my_dict={
        'head_msg':'Electrical Department',
        'sub_msg1':'HOD : Mr.Patil Deepak D.',
        'sub-msg2':'Qualification : M.E., BE(Electronics)',
        'sub_msg3':'Teaching Experience : 11 yrs 6 months',
        'sub_msg4':'WELCOME TO DEPARTMENT OF ELECTRICAL ENGINEERING',
        'sub_msg5':'This new age, the age of Technology, dawned with the discovery of Electricity and the subsequent development of Electrical Engineering. Equipped with modern infrastructure and supported by a team of competent faculty members , the Electrical Department at Yashwantrao Bhonsale Institute of Technology, Sawantwadi was set up in 2014. The key strengths of the department are qualified staff, established labs, Integrity in work, motivation, systematic process approach, Liberal work environment, student and staff feedback system, Yashwantrao Bhonsale Institute of Technology understands the importance of Electrical Engineering and is fully capable of meeting the expectations of young aspiring Engineers. The Electrical Engineering Department emphasizes on rigorous training in analytical and experimental techniques, effectively giving students an integrated approach and a thorough understanding of how to solve the problems and more importantly, equip them to face the challenges in Industry.',
        'sub_msg6':'EESA (ELECTRICAL ENGINEERING STUDENTS ASSOCIATION) was formed in the year 2014-2015.Main objective of EESA committee is to provide platform for the students in event management. The event include co-curricular, departmental, inter departmental and inter institutional and national level. Students also organize workshops inviting eminent personalities from both industry and academics.',
    }
    return render(request,'elec.html',context=my_dict)

def mechanical(request):
    my_dict={
        'head_msg':'Mechanical Department',
        'sub_msg1':'HOD : Mr. Rane Abhishek J.',
        'sub_msg2':'Qualification : M.E.Mechanical',
        'sub_msg3':'Teaching Experience : 10 yrs 3 months',
        'sub_msg4':'abhi27.rane@gmail.com',
        'sub_msg5':'WELCOME TO DEPARTMENT OF MECHANICAL ENGINEERING',
        'sub_msg6':'Mechanical Engineering Department was established in 2014. The intake capacity of students is 120. The department has highly qualified and experienced faculty with expertise in the areas of Design, Production, Manufacturing, CAD/CAM, Automobile and Thermal. The department believes in delivering the employability skill based and practical based education to the students. Numbers of pass out students are serving in various Manufacturing units, Automobile Industries, & even in Government departments. Few students started their own small scale industries.',
        'sub_msg7':'Well-equipped laboratories, departmental library, workshop with good infrastructure are the strength of the department. Knowledge of modern trends in industries like CNC machines, various software’s etc. is also imparted for development of students. We also participate in various activities of M.S.B.T.E., Mumbai. In-Plant training, Placement, Guest Lectures, Visits, Personality Development, Seminars, Career Guidance programs are arranged for getting all round engineers needed for fulfilling market need of trained manpower with soft skills. The Department provides career guidance to students for Higher Education as well as Entrepreneurship.',
        'sub_msg8':'The Department continuously encourages their students to participate in various activities like Industry Based Project Work, apart from placement. Students from the department won number of prizes in various project competitions, Quiz competitions, paper presentations, poster presentation & even in various sport activities.',
        'sub_msg9':'MESA, the Mechanical Engineering Students Association of YBIT Sawantwadi, aims to play a pivotal role in the development of students as engineers by various out-of-curriculum and extra curricular activities. By way of its activities MESA aims to be a platform for all the students of YBIT Sawantwadi in general and particularly of the students of ME department. MESA seeks to be an active organization of the ME department at YBIT Sawantwadi which will promotes their career interests.',
    }
    return render(request,'mech.html',context=my_dict)
    
def civil(request):
    my_dict={
        'head_msg':'Civil Department',
        'sub_msg1':'HOD : Mr. Sawant Prasad P.',
        'sub_msg2':'Qualification : M.E.Civil, B.E. (Civil)',
        'sub_msg3':'Teaching Experience : 11 yrs',
        'sub_msg4':'sawantpp85@gmail.com',
        'sub_msg5':'WELCOME TO DEPARTMENT OF CIVIL ENGINEERING',
        'sub_msg6':'Civil engineering is the oldest engineering discipline, is being offered at this institute from the academic year 2014. This department is endowed with a high caliber, dedicated, well qualified and experienced team of professionally inclined faculty. To sustain global competition, innovative techniques will be utilized to expose the students to the latest trends and practices in the construction industry through various activities like site visits, seminars by experts from fields and technical projects.',
        'sub_msg7':'The main objective of the Departments is to provide students with the necessary skills and practical experience to fulfill their professional duties and responsibilities in teamwork, along with ethics, technical leadership, business acumen and lifelong learning. This will provide the path for the students to become a future engineer, innovators and make substantial contributions to the society of Civil Engineers.',
        'sub_msg8':'Civil Engineering Student Association (CESA) is a student association run by students of Civil Engineering department. The main aim of the CESA is to provide platform to students to explore their skills and knowledge through curricular and extra-curricular activities in the field of Civil Engineering. CESA is dedicated to the overall development of students by organizing various Technical events on various occasions, like “Teachers Day” and "Engineers Day". We at CESA regularly organize workshops, guest lectures, expert talks, social events and various technical events for the benefit of students.',
    }
    return render(request,'civil.html',context=my_dict)
def index(request):
    return render(request,'index.html')
    


