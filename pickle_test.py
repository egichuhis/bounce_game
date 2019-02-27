import pickle


list_fav = ['mastery', 'humility', 'progress', 'service']
save_fav = open('save.dat', 'wb')
pickle.dump(list_fav, save_fav)
save_fav.close()

load_fav = open('save.dat', 'rb')
loaded_list_fav = pickle.load(load_fav)
load_fav.close()


print(loaded_list_fav)