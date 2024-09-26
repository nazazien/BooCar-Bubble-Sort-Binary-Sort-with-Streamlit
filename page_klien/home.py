from keperluan_modul import *
bg()

show_pages([
    Page("page_klien/home.py", "🏠 Home"),              
    Page("page_klien/cek_booking.py", "📅 Check Queue"),
    Page("page_klien/daftar_booking_servis.py", "🚗 Register Service Booking"),                    
    Page("page_klien/rating_dan_ulasan.py", "🌟 FeedBacks"),    
    Page("about_us.py", "👤 About Us"),                                            
])

st.header(':rainbow[BooCare by BoiCode?]', divider='rainbow')
st.title('CAR SERVICE BOOKING APPLICATION')
st.write(':grey[Thursday, April 4 2024 at 2:48:11 PM]')
st.title('')

st.subheader('WANT TO SERVICE YOUR CAR HERE?')
st.image(Image.open('img/mobil.jpg'), width=500, caption='Source: https://storyset.com/')
st.subheader('What is BooCare?')
st.markdown('''BooCare is a Car Service Booking application. This service provides customers with the convenience of scheduling their 
            service visits to authorized workshops, thereby shortening the waiting time from long queues. This will certainly make it 
            easier for customers to manage their service visit schedules to authorized workshops according to their needs. 
            :rainbow[Come on, try it now here!]''')
