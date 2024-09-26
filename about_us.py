from keperluan_modul import *
bg()

st.header(':rainbow[ABOUT US]', divider='rainbow')
st.subheader('We are behind the scenes of BooCar!')
st.subheader("")

deskripsi, poto = st.columns([3,2])
with deskripsi:
    st.markdown('''Welcome to BooCar's "About Us" page! We are the "BooiCode" team from class 2023E of the Data Science study program at the Faculty of Mathematics and Natural Sciences, Surabaya State University. Under the guidance of Mrs. Fadhilah Qalbi Annisa, S.T., M.Sc., we have put our efforts into developing innovative applications in order to fulfill the final semester assignment for the Data Structures and Algorithms course.''')

with poto:
    st.image(Image.open('img/logo.png'), width=200)
    
st.markdown('''\n\nBooCar is an online car service booking application that we created. This application aims to make it easier for users to order car service services online. With BooCar, users can easily book a service date before servicing their car, providing convenience and comfort for our customers. 
            
            \nIn developing BooCar, we implemented a combination of data structures and algorithms, especially Linked List, Bubble Sort, and Binary Search. We are confident that by utilizing the latest technology and concepts in the field of Data Structures and Algorithms, BooCar will be an efficient and reliable solution for customers' needs in caring for their cars. 
            
            \nThank you for visiting our "About Us" page. We are committed to continuing to improve BooCar in order to provide better and more satisfying services for our users.''')


st.subheader("",divider='grey')
st.subheader(":rainbow[Our Team]", divider='grey')

col1,col2,col3 = st.columns([2,2,2])
with col1:
    st.image(Image.open('img/us/naza.jpg'), width=150)
    st.markdown('''Naza Sulthoniyah Wahda
                23031554026
                naza.23026@gmail.com''')
with col2:
    st.image(Image.open('img/us/fakhriatu.jpg'), width=150)
    st.markdown('''Fakhriatul J Koni
                23031554186
                fakhriatu.23186@mhs.unesa.ac.id''')
with col3:
    st.image(Image.open('img/us/salsa.jpg'), width=150)
    st.markdown('''Salsabilla Indah Rahmawati
                23031554193
                salsabilla.23193@mhs.unesa.ac.id''')