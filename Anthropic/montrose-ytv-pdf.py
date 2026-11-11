from fpdf import FPDF

# Transcript data for Montrose Regional Health podcast with Dr. Williams
transcript_data = [
    ("[00:00:00]", "foreign"),
    ("[00:00:01]", "[Music]"),
    ("[00:00:03]", "Square Media mantras I'm Belinda haddock and today I have the pleasure of speaking with Dr Williams our community's new rheumatologist at"),
    ("[00:00:12]", "Montrose Regional Health good morning good morning and it's a pleasure for me to participate in this podcast yes and"),
    ("[00:00:20]", "thank you for doing so so I've got some questions for you that people might want to know where are you from originally Dr Williams I have a somewhat convoluted"),
    ("[00:00:29]", "story my father was in the United States Army and he had the opportunity originating from Mississippi to go to"),
    ("[00:00:38]", "France as part of his service requirement and he went there met my mother who was French and I was"),
    ("[00:00:46]", "subsequently born in France at a U.S army Hospital on an American Basin"),
    ("[00:00:53]", "Verdun France and we lived there until I was about four years old French was my"),
    ("[00:01:00]", "first language and as a compromise my parents their compromise they decided"),
    ("[00:01:08]", "between Mississippi and France that they would move to Memphis Tennessee oh wow I essentially grew up in Memphis Tennessee"),
    ("[00:01:17]", "I did my undergraduate work at Memphis State University I did graduate work at"),
    ("[00:01:24]", "the Memphis at Memphis State University and I also attended the University of Tennessee College of Medicine which is"),
    ("[00:01:32]", "also in Memphis Tennessee so that's where I came from a long roundabout way do you remember French still oh yeah"),
    ("[00:01:41]", "yeah uh we until maybe in the last decade we still had relatives that were"),
    ("[00:01:47]", "living and my wife and I had frequently visited France and as a child we did go"),
    ("[00:01:54]", "back on occasion at that time you had to dress up in a suit to ride in a Jet Plane it was a big experience"),
    ("[00:02:03]", "yep yep I remember those days all right and so Dr Williams do you what are some of your interests"),
    ("[00:02:12]", "I'll travel and explore as it does my wife so we spend a lot of our time Outdoors we bike we hike we like"),
    ("[00:02:20]", "exploring new Vistas new places meeting new people we like to do it on the local level uh not so much the tourist level"),
    ("[00:02:29]", "we like to actually engage the inhabitants of whatever community that"),
    ("[00:02:36]", "we are visiting or living with I'm also interested in astronomy I have a nice telescope into my detriment you know"),
    ("[00:02:44]", "after living in Denver for 30 years the only things I can see are the Sun the"),
    ("[00:02:51]", "moon and a couple of the planets nothing else shows up in Denver well luckily you're going to be here it's going to"),
    ("[00:02:58]", "change when you get here for sure I'm looking forward to that I think you have a completely different Sky than what I'm used to yeah yeah depending on where you"),
    ("[00:03:07]", "live most of the time it's very dark you've probably see very well yeah so I'm really looking forward to that all"),
    ("[00:03:13]", "right so those those are the major things that I'm interested in and mantras has a large variety of biking"),
    ("[00:03:22]", "and hiking trails too and all right around here as a matter of fact so I'm sure you'll enjoy it oh yeah and we're looking forward to going to the Western"),
    ("[00:03:30]", "Slope simply because we're still in Colorado Colorado is a fantastic State and uh we have explored you know our"),
    ("[00:03:39]", "environment locally here in Denver and uh and we've been through uh the western slope of the Grand Valley a few times"),
    ("[00:03:47]", "and uh but but all that area is unfamiliar to us so we are ecstatic about visiting all that there is to"),
    ("[00:03:54]", "offer I'm sure you'll have a good time and there are lots of things to explore right here on Western Slope yes we're looking forward to it and so Dr Williams"),
    ("[00:04:03]", "what is a rheumatologist okay a rheumatologist is a sub-specialist that"),
    ("[00:04:11]", "has been trained in Internal Medicine the field of room Dermatology is kind of widespread it encompasses everything"),
    ("[00:04:20]", "from treating musculoskeletal ailments to dealing with autoimmune disorders"),
    ("[00:04:26]", "such as lupus erythematosus or rheumatoid arthritis it delves into diagnosis and management of pain"),
    ("[00:04:36]", "syndromes fibromyalgia is a commonly known one we also deal with over a hundred"),
    ("[00:04:44]", "different types of arthritis most prominently is probably rheumatoid arthritis in terms of an autoimmune or"),
    ("[00:04:51]", "inflammatory aspect there is also mechanical or degenerative arthritis"),
    ("[00:04:58]", "including osteoarthritis which plagues a large number of people there is a gout there are muscle"),
    ("[00:05:07]", "disorders blood vessel disorders contrary to popular beliefs uh I do not"),
    ("[00:05:14]", "treat just the elderly uh it is not only the elderly that have arthritis symptoms"),
    ("[00:05:20]", "in fact the most common denominator in terms of autoimmune disorders is that of"),
    ("[00:05:27]", "females of reproductive age so actually for a rheumatologist the majority of their patient population is in the"),
    ("[00:05:35]", "category of young females which is a misconception because most people think arthritis only afflicts you as you get"),
    ("[00:05:44]", "older and that's not true right uh you can have you can have arthritis of an inflammatory basis uh in two years old"),
    ("[00:05:53]", "and from there on so it's widespread the other thing that I find particularly fascinating that in addition to the"),
    ("[00:06:00]", "musculoskeletal aspects of Rheumatology and the arthritic aspects a lot of our"),
    ("[00:06:07]", "disorders can especially if they're inflammatory and on an autoimmune basis they can involve other organ systems"),
    ("[00:06:15]", "such as the brain and the nervous system the blood vessels the hearts the lungs"),
    ("[00:06:21]", "the kidneys virtually we have to keep up to date in the management diagnosis of"),
    ("[00:06:28]", "these orders because it's not just relegated to joints and the articular system in fact autoimmune disorders of"),
    ("[00:06:37]", "an inflammatory nature can cause problems in virtually all organ systems including the skin the eyes so it's it's"),
    ("[00:06:46]", "uh it's widespread and that that helps maintain my interest because it is just more than what someone wants sick is"),
    ("[00:06:54]", "treating arthritis of the joints and so is that what Drew you to become a rheumatologist is all of the different"),
    ("[00:07:02]", "aspects of it that's part of it what initially drew me to Rheumatology is"),
    ("[00:07:09]", "first of all I was looking to sub-specialize in Internal Medicine and I looked at a variety of subspecialties"),
    ("[00:07:16]", "and Rheumatology appealed to me because and a lot of disorders and sub-specialties and Internal Medicine"),
    ("[00:07:24]", "the disorders are sometimes related to lifestyle decisions that patients make"),
    ("[00:07:30]", "whereas in Rheumatology it appeared that you know it's the luck of the draw for the majority of it there are genetic"),
    ("[00:07:38]", "elements and there are hereditary factors there are certainly environmental factors but it was it was basically you roll the dice as to"),
    ("[00:07:46]", "whether or not you're going to get one of the disorders that I treat and uh that appealed to me what also appealed"),
    ("[00:07:54]", "to me is I have a background in biology and specifically cell and molecular biology and there's a lot of cell and molecular"),
    ("[00:08:04]", "biology that has as its background in Rheumatology there's a lot of science that appeals to me and it especially"),
    ("[00:08:12]", "becoming more so on the Forefront the other thing that really appealed to me is that the time that I contemplated"),
    ("[00:08:20]", "going into Rheumatology there was not much known most of the treatments were basically to improve the patient's"),
    ("[00:08:29]", "well-being and their symptoms there were no agents on hand Methotrexate was just coming around as the anchor drug we were"),
    ("[00:08:38]", "still using gold injections and oral gold which was somewhat assertive and hydroxychloroquine and aside from"),
    ("[00:08:46]", "corticosteroids that was basically all the options that we had for treating autoimmune disorders well thankfully I"),
    ("[00:08:53]", "chose correctly because the field has exploded in terms of diagnosis and and"),
    ("[00:09:00]", "in management and with a flurry of multiple biologic agents that at least"),
    ("[00:09:07]", "continuate if not relieved the symptoms which is very encouraging to me I think"),
    ("[00:09:14]", "there will be at some point in the future you will not be able to see a patient that has debilitating arthritis and that you can visibly recognize them"),
    ("[00:09:23]", "due to deformities so that is that is very encouraging to me uh that we can actually"),
    ("[00:09:30]", "maybe not so much cure but we can put into remission for the majority uh their"),
    ("[00:09:37]", "symptoms and that's probably very encouraging to our listeners as well anyone that's experiencing that"),
    ("[00:09:44]", "persistent joint pain or stiffness I was reading earlier that the CDC arthritis is reported by at least a one in six"),
    ("[00:09:52]", "adults in every state with women having a higher prevalence in Most states so I think there's a lot of people that are"),
    ("[00:09:59]", "going to find benefit of you coming to our community well that's that's welcome news because I enthusiastically look"),
    ("[00:10:07]", "forward to my contributions to improving the overall health of the community and I know that there's been a deficit in in"),
    ("[00:10:14]", "terms of Rheumatology issues and hopefully I will be able to fulfill the community's needs and I'm sure that you"),
    ("[00:10:23]", "will can you tell us what you enjoy most about being a rheumatologist Rheumatology uh as is internal medicine"),
    ("[00:10:30]", "listen it's kind of like detective work you have to sometimes especially Rheumatology put together a variety of"),
    ("[00:10:39]", "complaints that necessarily don't point to one thing so there's that aspect of it you there's a lot of deduction I used"),
    ("[00:10:47]", "to read Sherlock Holmes as a kid and that's always kind of influenced me a little bit in terms of trying to figure"),
    ("[00:10:54]", "out you know the specific complaints and what's causing them in a particular patient the approach that I use though"),
    ("[00:11:01]", "is you or I tend to rule out what a person's symptoms might be instead of a"),
    ("[00:11:11]", "rheumatological disorder because there are a lot of signs and symptoms that could be related to something else and"),
    ("[00:11:18]", "is not necessarily due to a rheumatological or disorder if you look at frequency of occurrence it's more"),
    ("[00:11:26]", "likely that a person will have a disorder that is not of room technological Origins than a true"),
    ("[00:11:34]", "rheumatological or especially an autoimmune disorder that's causing their issues so that's that's the part of it kind of parenting out what the"),
    ("[00:11:42]", "subtleties are in establishing the diagnosis and I believe it's instead of just shotgunning and making this kind of"),
    ("[00:11:50]", "a generalized diagnosis you have to be very specific because the agents that we treat patients with are very specific"),
    ("[00:11:56]", "and have to be selected carefully on the basis of going for making an improvement in their overall health so I like the"),
    ("[00:12:05]", "detective work aspect of it I also get a lot of satisfaction in establishing diagnoses in people that had symptoms"),
    ("[00:12:13]", "that didn't know what they had maybe their primary care practitioner didn't know what they had exactly and when I"),
    ("[00:12:22]", "can kind of come in and offer a maybe a unifying diagnosis that gives me a sense"),
    ("[00:12:29]", "of self status faction the thing I really enjoy though is just the the interaction on a human to human level in"),
    ("[00:12:37]", "terms of trying to deliver the best health care that I can and then doing so I like to work with the patient I like"),
    ("[00:12:46]", "to work with the patients Primary Care practitioners or any other providers that they have so that it's kind of a"),
    ("[00:12:53]", "team effort and that's what I enjoy too I like the multi-disciplinary aspect of rheumatology because frequently I will be involved"),
    ("[00:13:02]", "with discussions and interactions with neurologists or cardiologists or pulmonologist or nephrologist it's a"),
    ("[00:13:12]", "physical therapists occupational therapist so there's a whole gamut of people that are involved in taking care"),
    ("[00:13:20]", "of individuals with Rheumatic disease doing all the detective work putting together the pieces of the puzzle and then making sure that your patients are"),
    ("[00:13:27]", "living their best possible life and living life each day feeling their best yeah absolutely and and my Approach is I"),
    ("[00:13:37]", "would I treat everyone equally I treat everyone as"),
    ("[00:13:44]", "how I would like to be treated if I were interacting with a physician the Golden Rule absolutely"),
    ("[00:13:51]", "well all right we look forward to having you here in the Montrose Community with Montrose Regional Health hopefully we'll"),
    ("[00:13:58]", "see you very soon thank you B I've enjoyed our conversation and I hope this will give"),
    ("[00:14:06]", "our listeners a better idea as to what I will be doing in Montrose and I really look forward to being there and part of"),
    ("[00:14:14]", "the community and we look forward to having you Dr Williams thank you so much for taking the time to speak with us today my pleasure thank you so much Pete"),
    ("[00:14:23]", "and Dr Williams will be starting his tenure in Montrose August 1st at Montrose Rheumatology LLC which is"),
    ("[00:14:30]", "located at Peak professionals 1550 Niagara Road in Montrose thank you for listening to this Montrose regional"),
    ("[00:14:37]", "health update information provided in this podcast is for informational and educational purposes only and is not meant to diagnose any condition or"),
    ("[00:14:45]", "provide treatment advice please work with your health care providers to determine appropriate treatments for you")
]

# Build PDF using fpdf2
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=20)
pdf.add_page()

# Header
pdf.set_fill_color(52, 152, 219)
pdf.set_text_color(255, 255, 255)
pdf.set_font("Helvetica", "B", 18)
pdf.cell(0, 15, "Montrose Regional Health Podcast", new_x="LMARGIN", new_y="NEXT", align="C", fill=True)
pdf.set_font("Helvetica", "", 10)
pdf.cell(0, 10, "Interview with Dr. Williams - Rheumatologist", new_x="LMARGIN", new_y="NEXT", align="C", fill=True)
pdf.ln(10)

# Transcript lines
pdf.set_text_color(26, 60, 90)
for ts, txt in transcript_data:
    pdf.set_font("Courier", "B", 9)
    pdf.set_text_color(41, 128, 185)
    ts_width = 28
    x_start = pdf.get_x()
    y_start = pdf.get_y()
    pdf.cell(ts_width, 5, ts)

    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(26, 60, 90)
    pdf.multi_cell(0, 5, txt)
    pdf.ln(2)

# Footer
pdf.ln(10)
pdf.set_draw_color(189, 195, 199)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())
pdf.ln(5)
pdf.set_font("Helvetica", "I", 8)
pdf.set_text_color(127, 140, 141)
pdf.cell(0, 5, "Montrose Regional Health Update - For informational and educational purposes only", align="C")

output_pdf = "Montrose_Dr_Williams_Transcript.pdf"
pdf.output(output_pdf)
print(output_pdf)
