# -*- coding: utf-8 -*-
'''
      * ***       ***      ***      *******
    *  ****     ** ***   ** ***   *       ***                           *
   *  *  ***   **   *** **   *** *         **                          ***
  *  **   ***  **       **       **        *                            *
 *  ***    *** **       **        ***             ****   ***  ****
**   **     ** ******   ******   ** ***          * ***  * **** **** * ***   ***  ****     ****
**   **     ** *****    *****     *** ***       *   ****   **   ****   ***   **** **** * *  ***  *
**   **     ** **       **          *** ***    **    **    **           **    **   **** *    ****
**   **     ** **       **            *** ***  **    **    **           **    **    ** **     **
**   **     ** **       **              ** *** **    **    **           **    **    ** **     **
 **  **     ** **       **               ** ** **    **    **           **    **    ** **     **
  ** *      *  **       **                * *  **    **    **           **    **    ** **     **
   ***     *   **       **      ***        *   *******     ***          **    **    ** **     **
    *******    **       **     *  *********    ******       ***         *** * ***   *** ********
      ***       **       **   *     *****      **                        ***   ***   ***  *** ***
                              *                **                                              ***
                               **              **                                        ****   ***
                                                **                                     *******  **
                                                                                      *     ****
'''

import os,sys

import six

from resources.lib.modules import control
from resources.lib.modules import trakt
from resources.lib.modules import cache

sysaddon = sys.argv[0] ; syshandle = int(sys.argv[1])

artPath = control.artPath() ; addonFanart = control.addonFanart()

imdbCredentials = False if control.setting('imdb.user') == '' else True

traktCredentials = trakt.getTraktCredentialsInfo()

traktIndicators = trakt.getTraktIndicatorsInfo()

queueMenu = six.ensure_str(control.lang(32065))


class navigator:
    def root(self):
        self.addDirectoryItem('[COLOR yellowgreen]Poison[/COLOR] IMDB Lists', 'poisonIMDBNavigator', 'list.png', 'DefaultMovies.png')
        self.addDirectoryItem('[COLOR yellowgreen]Poison[/COLOR] Movie Lists' , 'listNavigator', 'list.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32001, 'movieNavigator', 'movies.png', 'DefaultMovies.png')
        self.addDirectoryItem(32002, 'tvNavigator', 'tvshows.png', 'DefaultTVShows.png')

        if not control.setting('lists.widget') == '0':
            self.addDirectoryItem(32003, 'mymovieNavigator', 'mymovies.png', 'DefaultVideoPlaylists.png')
            self.addDirectoryItem(32004, 'mytvNavigator', 'mytvshows.png', 'DefaultVideoPlaylists.png')

        if not control.setting('movie.widget') == '0':
            self.addDirectoryItem(32005, 'movieWidget', 'latest-movies.png', 'DefaultRecentlyAddedMovies.png')

        if (traktIndicators == True and not control.setting('tv.widget.alt') == '0') or (traktIndicators == False and not control.setting('tv.widget') == '0'):
            self.addDirectoryItem(32006, 'tvWidget', 'latest-episodes.png', 'DefaultRecentlyAddedEpisodes.png')

        if not control.setting('channels') == '0':
            self.addDirectoryItem(32007, 'channels', 'channels.png', 'DefaultMovies.png')

        if not control.setting('furk.api') == '':
            self.addDirectoryItem('Furk.net', 'furkNavigator', 'movies.png', 'movies.png')
        self.addDirectoryItem(32008, 'toolNavigator', 'tools.png', 'DefaultAddonProgram.png')

        downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0 or len(control.listDir(control.setting('tv.download.path'))[0]) > 0) else False
        if downloads == True:
            self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultFolder.png')

        self.addDirectoryItem(32010, 'searchNavigator', 'search.png', 'DefaultFolder.png')

        self.endDirectory()

    def poisonimdb(self, lite=False):
        self.addDirectoryItem('[COLOR yellowgreen]Poison[/COLOR]', 'poison', 'list.png', 'DefaultMovies.png')
#        self.addDirectoryItem('NAME1', 'NAME1', 'icon.png', 'DefaultMovies.png')
#        self.addDirectoryItem('NAME2', 'NAME2', 'icon.png', 'DefaultMovies.png')
        self.endDirectory()

    def poison(self, lite=False):
        self.addDirectoryItem('New Movies (Some movies may NOT play until streaming is available)', 'movies&url=poisonpicks', 'list.png', 'DefaultMovies.png')
        self.addDirectoryItem('Creep Shows', 'movies&url=poisoncreep', 'list.png', 'DefaultMovies.png')
        self.addDirectoryItem('Space Odyssey', 'movies&url=poisonspace', 'list.png', 'DefaultMovies.png')
        self.addDirectoryItem('Wild West', 'movies&url=poisonwildw', 'list.png', 'DefaultMovies.png')
        self.addDirectoryItem('Docs', 'movies&url=poisondocs', 'list.png', 'DefaultMovies.png')
        self.addDirectoryItem('Breaking Law TV', 'tvshows&url=poisonbreak', 'list.png', 'DefaultTVShows.png')
        self.addDirectoryItem('World of Wheels TV', 'tvshows&url=poisonwow', 'list.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Game of Shows TV', 'tvshows&url=poisongos', 'list.png', 'DefaultTVShows.png')
        self.endDirectory()

    def listnav(self):
        self.addDirectoryItem ('[COLOR yellowgreen]Poison[/COLOR] [COLOR white]New Movie 1Clicks[/COLOR] [COLOR dodgerblue][Real Debrid][/COLOR]', 'lists', 'list.png', 'DefaultTVShows.png')
        self.addDirectoryItem ('[COLOR springgreen]Loonatics[/COLOR] [COLOR white]Movies 1Clicks[/COLOR] [COLORred][Non Debrid][/COLOR]', 'lista', 'list.png', 'DefaultTVShows.png')
        self.addDirectoryItem ('[COLOR red]Horror[/COLOR] [COLOR white]1Clicks[/COLOR] [COLOR dodgerblue][Real Debrid][/COLOR]', 'listb', 'list.png', 'DefaultTVShows.png')
        #self.addDirectoryItem (32489, 'listd', 'list.png', 'DefaultTVShows.png')
        #self.addDirectoryItem(32489, 'listd', 'list.png', 'DefaultTVShows.png')
        #self.addDirectoryItem(32490, 'liste', 'list.png', 'DefaultTVShows.png')
        #self.addDirectoryItem(32491, 'listf', 'list.png', 'DefaultTVShows.png')
        #self.addDirectoryItem(32492, 'listg', 'list.png', 'DefaultTVShows.png')
        #self.addDirectoryItem(32493, 'listh', 'list.png', 'DefaultTVShows.png')
        #self.addDirectoryItem(32494, 'kidsi', 'list.png', 'DefaultTVShows.png')
        #self.addDirectoryItem(32495, 'listj', 'list.png', 'DefaultTVShows.png')
        #self.addDirectoryItem(32496, 'listk', 'list.png', 'DefaultTVShows.png')
        #self.addDirectoryItem(32497, 'listl', 'list.png', 'DefaultTVShows.png')
        #self.addDirectoryItem(32498, 'listm', 'list.png', 'DefaultTVShows.png')
        #self.addDirectoryItem(32499, 'listn', 'list.png', 'DefaultTVShows.png')
        #self.addDirectoryItem(32500, 'listo', 'list.png', 'DefaultTVShows.png')
        #self.addDirectoryItem(32504, 'listp', 'list.png', 'DefaultTVShows.png')
        self.endDirectory()

    def furk(self):
        self.addDirectoryItem('User Files', 'furkUserFiles', 'mytvnavigator.png', 'mytvnavigator.png')
        self.addDirectoryItem('Search', 'furkSearch', 'search.png', 'search.png')
        self.endDirectory()

    def movies(self, lite=False):
        self.addDirectoryItem(32011, 'movieGenres', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem(32012, 'movieYears', 'years.png', 'DefaultMovies.png')
        self.addDirectoryItem(32123, 'movieDecades', 'years.png', 'DefaultMovies.png')
        self.addDirectoryItem(32013, 'moviePersons', 'people.png', 'DefaultMovies.png')
        self.addDirectoryItem(32014, 'movieLanguages', 'languages.png', 'DefaultMovies.png')
        self.addDirectoryItem(32015, 'movieCertificates', 'certificates.png', 'DefaultMovies.png')
        #self.addDirectoryItem(32017, 'movies&url=trending', 'trending.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32018, 'movies&url=popular', 'most-popular.png', 'DefaultMovies.png')
        self.addDirectoryItem(32019, 'movies&url=views', 'most-voted.png', 'DefaultMovies.png')
        self.addDirectoryItem(32020, 'movies&url=boxoffice', 'box-office.png', 'DefaultMovies.png')
        self.addDirectoryItem(32021, 'movies&url=oscars', 'oscar-winners.png', 'DefaultMovies.png')
        self.addDirectoryItem(32022, 'movies&url=theaters', 'in-theaters.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32005, 'movieWidget', 'latest-movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32124, 'customNavigator', 'imdb.png', 'DefaultMovies.png')
        self.addDirectoryItem(32125, 'imdbLists', 'imdb.png', 'DefaultMovies.png')
        #self.addDirectoryItem('Movie Mosts', 'movieMosts', 'most.png', 'fanart.jpg')

        if lite == False:
            if not control.setting('lists.widget') == '0':
                self.addDirectoryItem(32003, 'mymovieliteNavigator', 'mymovies.png', 'DefaultVideoPlaylists.png')

            self.addDirectoryItem(32028, 'moviePerson', 'people-search.png', 'DefaultMovies.png')
            self.addDirectoryItem(32010, 'movieSearch', 'search.png', 'DefaultMovies.png')

        self.endDirectory()


    def mymovies(self, lite=False):
        self.accountCheck()

        if traktCredentials == True and imdbCredentials == True:
            self.addDirectoryItem(32094, 'movies&url=onDeck', 'trakt.png', 'DefaultMovies.png', queue=True)
            self.addDirectoryItem(32032, 'movies&url=traktcollection', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
            if control.setting('imdb.sort.order') == '1':
                self.addDirectoryItem(32034, 'movies&url=imdbwatchlist2', 'imdb.png', 'DefaultMovies.png', queue=True)
            else:
                self.addDirectoryItem(32034, 'movies&url=imdbwatchlist', 'imdb.png', 'DefaultMovies.png', queue=True)
            self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))
            self.addDirectoryItem(32036, 'movies&url=trakthistory', 'trakt.png', 'DefaultMovies.png', queue=True)
            self.addDirectoryItem(32035, 'movies&url=traktfeatured', 'trakt.png', 'DefaultMovies.png', queue=True)

        elif traktCredentials == True:
            self.addDirectoryItem(32094, 'movies&url=onDeck', 'trakt.png', 'DefaultMovies.png', queue=True)
            self.addDirectoryItem(32032, 'movies&url=traktcollection', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))
            self.addDirectoryItem(32036, 'movies&url=trakthistory', 'trakt.png', 'DefaultMovies.png', queue=True)
            self.addDirectoryItem(32035, 'movies&url=traktfeatured', 'trakt.png', 'DefaultMovies.png', queue=True)

        elif imdbCredentials == True:
            if control.setting('imdb.sort.order') == '1':
                self.addDirectoryItem(32034, 'movies&url=imdbwatchlist2', 'imdb.png', 'DefaultMovies.png', queue=True)
            else:
                self.addDirectoryItem(32034, 'movies&url=imdbwatchlist', 'imdb.png', 'DefaultMovies.png', queue=True)
            self.addDirectoryItem(32077, 'movies&url=featured', 'imdb.png', 'DefaultMovies.png', queue=True)

        self.addDirectoryItem(32039, 'movieUserlists', 'userlists.png', 'DefaultMovies.png')

        if lite == False:
            self.addDirectoryItem(32031, 'movieliteNavigator', 'movies.png', 'DefaultMovies.png')
            self.addDirectoryItem(32028, 'moviePerson', 'people-search.png', 'DefaultMovies.png')
            self.addDirectoryItem(32010, 'movieSearch', 'search.png', 'DefaultMovies.png')

        self.endDirectory()


    def tvshows(self, lite=False):
        self.addDirectoryItem(32011, 'tvGenres', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32016, 'tvNetworks', 'networks.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32014, 'tvLanguages', 'languages.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32015, 'tvCertificates', 'certificates.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32017, 'tvshows&url=trending', 'people-watching.png', 'DefaultRecentlyAddedEpisodes.png')
        self.addDirectoryItem(32018, 'tvshows&url=popular', 'most-popular.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32023, 'tvshows&url=rating', 'highly-rated.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32019, 'tvshows&url=views', 'most-voted.png', 'DefaultTVShows.png')
        self.addDirectoryItem('TV Show Mosts', 'showMosts', 'featured.png', 'fanart.jpg')
        self.addDirectoryItem(32024, 'tvshows&url=airing', 'airing-today.png', 'DefaultTVShows.png')
        #self.addDirectoryItem(32025, 'tvshows&url=active', 'returning-tvshows.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32026, 'tvshows&url=premiere', 'new-tvshows.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32006, 'calendar&url=added', 'latest-episodes.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)
        self.addDirectoryItem(32027, 'calendars', 'calendar.png', 'DefaultRecentlyAddedEpisodes.png')

        if lite == False:
            if not control.setting('lists.widget') == '0':
                self.addDirectoryItem(32004, 'mytvliteNavigator', 'mytvshows.png', 'DefaultVideoPlaylists.png')

            self.addDirectoryItem(32028, 'tvPerson', 'people-search.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32010, 'tvSearch', 'search.png', 'DefaultTVShows.png')

        self.endDirectory()


    def mytvshows(self, lite=False):
        try:
            self.accountCheck()

            if traktCredentials == True and imdbCredentials == True:

                self.addDirectoryItem(32094, 'calendar&url=onDeck', 'trakt.png', 'DefaultTVShows.png')
                self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
                if control.setting('imdb.sort.order') == '1':
                    self.addDirectoryItem(32034, 'tvshows&url=imdbwatchlist2', 'imdb.png', 'DefaultTVShows.png')
                else:
                    self.addDirectoryItem(32034, 'tvshows&url=imdbwatchlist', 'imdb.png', 'DefaultTVShows.png')
                self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))
                self.addDirectoryItem(32035, 'tvshows&url=traktfeatured', 'trakt.png', 'DefaultTVShows.png')
                self.addDirectoryItem(32036, 'calendar&url=trakthistory', 'trakt.png', 'DefaultTVShows.png', queue=True)
                self.addDirectoryItem(32037, 'calendar&url=progress', 'trakt.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)
                self.addDirectoryItem(32038, 'calendar&url=mycalendar', 'trakt.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)
                self.addDirectoryItem(32041, 'episodeUserlists', 'userlists.png', 'DefaultTVShows.png')

            elif traktCredentials == True:
                self.addDirectoryItem(32094, 'calendar&url=onDeck', 'trakt.png', 'DefaultTVShows.png')
                self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
                self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))
                self.addDirectoryItem(32035, 'tvshows&url=traktfeatured', 'trakt.png', 'DefaultTVShows.png')
                self.addDirectoryItem(32036, 'calendar&url=trakthistory', 'trakt.png', 'DefaultTVShows.png', queue=True)
                self.addDirectoryItem(32037, 'calendar&url=progress', 'trakt.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)
                self.addDirectoryItem(32038, 'calendar&url=mycalendar', 'trakt.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)
                self.addDirectoryItem(32041, 'episodeUserlists', 'userlists.png', 'DefaultTVShows.png')

            elif imdbCredentials == True:
                if control.setting('imdb.sort.order') == '1':
                    self.addDirectoryItem(32034, 'tvshows&url=imdbwatchlist2', 'imdb.png', 'DefaultTVShows.png')
                else:
                    self.addDirectoryItem(32034, 'tvshows&url=imdbwatchlist', 'imdb.png', 'DefaultTVShows.png')
                self.addDirectoryItem(32077, 'tvshows&url=trending', 'imdb.png', 'DefaultTVShows.png', queue=True)

            self.addDirectoryItem(32040, 'tvUserlists', 'userlists.png', 'DefaultTVShows.png')

            if lite == False:
                self.addDirectoryItem(32031, 'tvliteNavigator', 'tvshows.png', 'DefaultTVShows.png')
                self.addDirectoryItem(32028, 'tvPerson', 'people-search.png', 'DefaultTVShows.png')
                self.addDirectoryItem(32010, 'tvSearch', 'search.png', 'DefaultTVShows.png')

            self.endDirectory()
        except:
            print("ERROR")


    def custom(self, lite=False):################# Poseidon Playlists 1 (by Soulless) ####################
        self.addDirectoryItem('Anime', 'movies&url=anime', 'anime.png', 'fanart.jpg')
        self.addDirectoryItem('Avant Garde', 'movies&url=avant', 'avant.png', 'fanart.jpg')
        self.addDirectoryItem('Based On A True Story', 'movies&url=true', 'true.png', 'fanart.jpg')
        self.addDirectoryItem('Biker', 'movies&url=biker', 'biker.png', 'fanart.jpg')
        self.addDirectoryItem('B Movies', 'movies&url=bmovie', 'bmovie.png', 'fanart.jpg')
        self.addDirectoryItem('Breaking The Fourth Wall', 'movies&url=breaking', 'breaking.png', 'fanart.jpg')
        self.addDirectoryItem('Business', 'movies&url=business', 'business.png', 'fanart.jpg')
        self.addDirectoryItem('Capers', 'movies&url=caper', 'caper.png', 'fanart.jpg')
        self.addDirectoryItem('Car Chases', 'movies&url=car', 'chase.png', 'fanart.jpg')
        self.addDirectoryItem('Character Study', 'movies&url=char', 'character.png', 'fanart.jpg')
        self.addDirectoryItem('Chick Flix', 'movies&url=chick', 'chick.png', 'fanart.jpg')
        self.addDirectoryItem('Coming to Age', 'movies&url=coming', 'coming.png', 'fanart.jpg')
        self.addDirectoryItem('Competition', 'movies&url=competition', 'comps.png', 'fanart.jpg')
        self.addDirectoryItem('Cult', 'movies&url=cult', 'cult.png', 'fanart.jpg')
        self.addDirectoryItem('Cyberpunk', 'movies&url=cyber', 'cyber.png', 'fanart.jpg')
        self.addDirectoryItem('Drug Addiction', 'movies&url=drugs', 'drug.png', 'fanart.jpg')
        self.addDirectoryItem('Dystopia', 'movies&url=dystopia', 'dystopia.png', 'fanart.jpg')
        self.addDirectoryItem('Epic', 'movies&url=epic', 'epic.png', 'fanart.jpg')
        self.addDirectoryItem('Espionage', 'movies&url=espionage', 'espionage.png', 'fanart.jpg')
        self.addDirectoryItem('Experimental', 'movies&url=expiremental', 'experimental.png', 'fanart.jpg')
        #self.addDirectoryItem('Existential', 'movies&url=Existential', 'exis.png', 'fanart.jpg')
        self.addDirectoryItem('Fairy Tale', 'movies&url=fairytale', 'fairytale.png', 'fanart.jpg')
        #self.addDirectoryItem('Farce', 'movies&url=farce', 'farce.png', 'fanart.jpg')
        #self.addDirectoryItem('Femme Fatale', 'movies&url=femme', 'femme.png', 'fanart.jpg')
        self.addDirectoryItem('Futuristic', 'movies&url=futuristic', 'futuristic.png', 'fanart.jpg')
        self.addDirectoryItem('Heist', 'movies&url=heist', 'heist.png', 'fanart.jpg')
        #self.addDirectoryItem('High School', 'movies&url=highschool', 'highschool.png', 'fanart.jpg')
        self.addDirectoryItem('Horror Movie Remakes', 'movies&url=remakes', 'horror.png', 'fanart.jpg')
        self.addDirectoryItem('James Bond', 'movies&url=bond', 'bond.png', 'fanart.jpg')
        self.addDirectoryItem('Kidnapping', 'movies&url=kidnapped', 'kidnapped.png', 'fanart.jpg')
        self.addDirectoryItem('Kung Fu', 'movies&url=kungfu', 'kungfu.png', 'fanart.jpg')
        self.addDirectoryItem('Monster', 'movies&url=monster', 'monster.png', 'fanart.jpg')
        #self.addDirectoryItem('Movie Loners', 'movies&url=loners', 'loner.png', 'fanart.jpg')
        #self.addDirectoryItem('Movies & Racism', 'movies&url=racist', 'race.png', 'fanart.jpg')
        #self.addDirectoryItem('Neo Noir', 'movies&url=neo', 'neo.png', 'fanart.jpg')
        #self.addDirectoryItem('Parenthood', 'movies&url=parenthood', 'parenthood.png', 'fanart.jpg')
        #self.addDirectoryItem('Parody', 'movies&url=parody', 'parody.png', 'fanart.jpg')
        self.addDirectoryItem('Post Apocalypse', 'movies&url=apocalypse', 'apocalypse.png', 'fanart.jpg')
        self.addDirectoryItem('Private Eye', 'movies&url=private', 'dick.png', 'fanart.jpg')
        self.addDirectoryItem('Remakes', 'movies&url=remake', 'remake.png', 'fanart.jpg')
        #self.addDirectoryItem('Road Movies', 'movies&url=road', 'road.png', 'fanart.jpg')
        self.addDirectoryItem('Robots', 'movies&url=robot', 'robot.png', 'fanart.jpg')
        #self.addDirectoryItem('Satire', 'movies&url=satire', 'satire.png', 'fanart.jpg')
        #self.addDirectoryItem('Schizophrenia', 'movies&url=schiz', 'schiz.png', 'fanart.jpg')
        self.addDirectoryItem('Serial Killers', 'movies&url=serial', 'serial.png', 'fanart.jpg')
        self.addDirectoryItem('Slasher', 'movies&url=slasher', 'slasher.png', 'fanart.jpg')
        self.addDirectoryItem('Spiritual', 'movies&url=spiritual', 'spiritual.png', 'fanart.jpg')
        #self.addDirectoryItem('Spoofs', 'movies&url=spoof', 'spoof.png', 'fanart.jpg')
        self.addDirectoryItem('Star Wars', 'movies&url=star', 'starwars.png', 'fanart.jpg')
        self.addDirectoryItem('Steampunk', 'movies&url=steampunk', 'steampunk.png', 'fanart.jpg')
        self.addDirectoryItem('Superheros', 'movies&url=superhero', 'superhero.png', 'fanart.jpg')
        self.addDirectoryItem('Supernatural', 'movies&url=supernatural', 'supernatural.png', 'fanart.jpg')
        self.addDirectoryItem('Tech Noir', 'movies&url=tech', 'tech.png', 'fanart.jpg')
        self.addDirectoryItem('Time Travel', 'movies&url=time', 'time.png', 'fanart.jpg')
        self.addDirectoryItem('Vampires', 'movies&url=vampire', 'vampire.png', 'fanart.jpg')
        #self.addDirectoryItem('Virtual Reality', 'movies&url=vr', 'vr.png', 'fanart.jpg')
        #self.addDirectoryItem('Wilhelm Scream', 'movies&url=wilhelm', 'wilhelm.png', 'fanart.jpg')
        self.addDirectoryItem('Zombies', 'movies&url=zombie', 'zombie.png', 'fanart.jpg')
        self.addDirectoryItem('New Years', 'movies&url=newyear', 'newyears.png', 'fanart.jpg')
        self.addDirectoryItem('Easter', 'movies&url=easter', 'easter.png', 'fanart.jpg')
        self.addDirectoryItem('Halloween', 'movies&url=halloween', 'halloween.png', 'fanart.jpg')
        self.addDirectoryItem('Thanksgiving', 'movies&url=thanx', 'thanksgiving.png', 'fanart.jpg')
        self.addDirectoryItem('Christmas', 'movies&url=xmass', 'christmas.png', 'fanart.jpg')
        self.addDirectoryItem('DC', 'movies&url=dc', 'dc.png', 'fanart.jpg')
        self.addDirectoryItem('Disney and Pixar', 'movies&url=disney', 'pixar.png', 'fanart.jpg')
        self.addDirectoryItem('Marvel Universe', 'movies&url=marvel', 'marvel.png', 'fanart.jpg')

        self.endDirectory()


    def imdbLists(self):################# Poseidon Playlists 2 (by Soulless) ####################
        self.addDirectoryItem('Greatest Movies: 2000-2017', 'movies&url=imdb1', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Horror Movie Series', 'movies&url=imdb2', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Horror Of The Skull Posters', 'movies&url=imdb3', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Top Satirical Movies', 'movies&url=imdb4', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Greatest Science Fiction', 'movies&url=imdb5', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Famous and Infamous Movie Couples', 'movies&url=imdb6', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Top Private Eye Movies', 'movies&url=imdb7', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Sleeper Hit Movies', 'movies&url=imdb8', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Cult Horror Movies', 'movies&url=imdb9', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Heist Caper Movies', 'movies&url=imdb10', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Artificial Intelligence', 'movies&url=imdb11', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Stephen King Movies and Adaptations', 'movies&url=imdb12', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Alien Invasion', 'movies&url=imdb13', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Contract Killers', 'movies&url=imdb14', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Heroic Bloodshed', 'movies&url=imdb15', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Conspiracy', 'movies&url=imdb16', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Top Kung Fu', 'movies&url=imdb17', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Movies Based In One Room', 'movies&url=imdb18', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Movies For Intelligent People', 'movies&url=imdb19', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Inspirational Movies', 'movies&url=imdb20', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Tech Geeks', 'movies&url=imdb21', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Movie Clones', 'movies&url=imdb22', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Obscure Underrated Movies', 'movies&url=imdb23', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Smut and Trash', 'movies&url=imdb24', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Revenge', 'movies&url=imdb25', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Motivational', 'movies&url=imdb26', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Disaster & Apocalyptic', 'movies&url=imdb27', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Music or Musical Movies', 'movies&url=imdb28', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Mental, Physical Illness and Disability Movies', 'movies&url=imdb29', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Best Twist Ending Movies', 'movies&url=imdb30', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Heists, Cons, Scams & Robbers', 'movies&url=imdb31', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Road Trip & Travel', 'movies&url=imdb32', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Spy - CIA - MI5 - MI6 - KGB', 'movies&url=imdb33', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Prison & Escape', 'movies&url=imdb34', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Courtroom', 'movies&url=imdb35', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Father - Son', 'movies&url=imdb36', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Based on a True Story', 'movies&url=imdb37', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Man Vs. Nature', 'movies&url=imdb38', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Gangster', 'movies&url=imdb39', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Teenage', 'movies&url=imdb40', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Old Age', 'movies&url=imdb41', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Serial Killers', 'movies&url=imdb42', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Addiction', 'movies&url=imdb43', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Time Travel', 'movies&url=imdb44', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Puff Puff Pass', 'movies&url=imdb45', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Artists , Painters , Writers', 'movies&url=imdb46', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Love', 'movies&url=imdb47', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Winter Is Here', 'movies&url=imdb48', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Suicide', 'movies&url=imdb49', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Alchoholic', 'movies&url=imdb50', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Video Games', 'movies&url=imdb51', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Shocking Movie Scenes', 'movies&url=imdb52', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Biographical', 'movies&url=imdb53', 'imdb.png', 'fanart.jpg')
        self.addDirectoryItem('Movies to Teach You a Thing or Two', 'movies&url=imdb54', 'imdb.png', 'fanart.jpg')

        self.endDirectory()


    def movieMosts(self):
        self.addDirectoryItem('Most Played This Week', 'movies&url=played1', 'trakt.png', 'fanart.jpg')
        self.addDirectoryItem('Most Played This Month', 'movies&url=played2', 'trakt.png', 'fanart.jpg')
        self.addDirectoryItem('Most Played This Year', 'movies&url=played3', 'trakt.png', 'fanart.jpg')
        self.addDirectoryItem('Most Played All Time', 'movies&url=played4', 'trakt.png', 'fanart.jpg')
        self.addDirectoryItem('Most Collected This Week', 'movies&url=collected1', 'trakt.png', 'fanart.jpg')
        self.addDirectoryItem('Most Collected This Month', 'movies&url=collected2', 'trakt.png', 'fanart.jpg')
        self.addDirectoryItem('Most Collected This Year', 'movies&url=collected3', 'trakt.png', 'fanart.jpg')
        self.addDirectoryItem('Most Collected All Time', 'movies&url=collected4', 'trakt.png', 'fanart.jpg')
        self.addDirectoryItem('Most Watched This Week', 'movies&url=watched1', 'trakt.png', 'fanart.jpg')
        self.addDirectoryItem('Most Watched This Month', 'movies&url=watched2', 'trakt.png', 'fanart.jpg')
        self.addDirectoryItem('Most Watched This Year', 'movies&url=watched3', 'trakt.png', 'fanart.jpg')
        self.addDirectoryItem('Most Watched All Time', 'movies&url=watched4', 'trakt.png', 'fanart.jpg')

        self.endDirectory()

    def showMosts(self):
        self.addDirectoryItem('Most Played This Week', 'tvshows&url=played1', 'trakt.png', 'fanart.jpg')
        self.addDirectoryItem('Most Played This Month', 'tvshows&url=played2', 'trakt.png', 'fanart.jpg')
        self.addDirectoryItem('Most Played This Year', 'tvshows&url=played3', 'trakt.png', 'fanart.jpg')
        self.addDirectoryItem('Most Played All Time', 'tvshows&url=played4', 'trakt.png', 'fanart.jpg')
        self.addDirectoryItem('Most Collected This Week', 'tvshows&url=collected1', 'trakt.png', 'fanart.jpg')
        self.addDirectoryItem('Most Collected This Month', 'tvshows&url=collected2', 'trakt.png', 'fanart.jpg')
        self.addDirectoryItem('Most Collected This Year', 'tvshows&url=collected3', 'trakt.png', 'fanart.jpg')
        self.addDirectoryItem('Most Collected All Time', 'tvshows&url=collected4', 'trakt.png', 'fanart.jpg')
        self.addDirectoryItem('Most Watched This Week', 'tvshows&url=watched1', 'trakt.png', 'fanart.jpg')
        self.addDirectoryItem('Most Watched This Month', 'tvshows&url=watched2', 'trakt.png', 'fanart.jpg')
        self.addDirectoryItem('Most Watched This Year', 'tvshows&url=watched3', 'trakt.png', 'fanart.jpg')
        self.addDirectoryItem('Most Watched All Time', 'tvshows&url=watched4', 'trakt.png', 'fanart.jpg')

        self.endDirectory()

    def tools(self):
        self.addDirectoryItem('[B]Poison[/B] : Changelog', 'changelog', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32043, 'openSettings&query=0.0', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32556, 'libraryNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32049, 'viewsNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32604, 'clearCacheSearch', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32050, 'clearSources', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32116, 'clearDebridCheck', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32052, 'clearCache', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32611, 'clearAllCache', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32108, 'cleanSettings', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        #self.addDirectoryItem(32079, 'poisonscrapersettings', 'icon.png', 'DefaultAddonProgram.png', isFolder=False)
        if not control.condVisibility('System.HasAddon(script.module.poisonscrapers)'):
            self.addDirectoryItem('[B]PoisonScrapers[/B] : Install', 'installPoisonScrapers', 'open.png', 'DefaultAddonProgram.png', isFolder=False)
        else:
            self.addDirectoryItem(32082, 'poisonscrapersettings', 'open.png', 'DefaultAddonProgram.png', isFolder=False)
        if not control.condVisibility('System.HasAddon(script.module.orion)'):
            self.addDirectoryItem('[B]Orion[/B] : Install', 'installOrion', 'orion.png', 'DefaultAddonProgram.png', isFolder=False)
        else:
            self.addDirectoryItem(32080, 'orionsettings', 'orion.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32076, 'smuSettings', 'resolveurl.png', 'DefaultAddonProgram.png', isFolder=False)
        if trakt.getTraktCredentialsInfo():
            self.addDirectoryItem(32093, 'syncTraktStatus', 'trakt.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32073, 'authTrakt', 'trakt.png', 'DefaultAddonProgram.png', isFolder=False)

        self.endDirectory()

    def library(self):
        self.addDirectoryItem(32557, 'openSettings&query=6.0', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32558, 'updateLibrary&query=tool', 'library_update.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32559, control.setting('library.movie'), 'movies.png', 'DefaultMovies.png', isAction=False)
        self.addDirectoryItem(32560, control.setting('library.tv'), 'tvshows.png', 'DefaultTVShows.png', isAction=False)

        if trakt.getTraktCredentialsInfo():
            self.addDirectoryItem(32561, 'moviesToLibrary&url=traktcollection', 'trakt.png', 'DefaultMovies.png', isFolder=False)
            self.addDirectoryItem(32562, 'moviesToLibrary&url=traktwatchlist', 'trakt.png', 'DefaultMovies.png', isFolder=False)
            self.addDirectoryItem(32563, 'tvshowsToLibrary&url=traktcollection', 'trakt.png', 'DefaultTVShows.png', isFolder=False)
            self.addDirectoryItem(32564, 'tvshowsToLibrary&url=traktwatchlist', 'trakt.png', 'DefaultTVShows.png', isFolder=False)

        self.endDirectory()

    def downloads(self):
        movie_downloads = control.setting('movie.download.path')
        tv_downloads = control.setting('tv.download.path')

        if len(control.listDir(movie_downloads)[0]) > 0:
            self.addDirectoryItem(32001, movie_downloads, 'movies.png', 'DefaultMovies.png', isAction=False)
        if len(control.listDir(tv_downloads)[0]) > 0:
            self.addDirectoryItem(32002, tv_downloads, 'tvshows.png', 'DefaultTVShows.png', isAction=False)

        self.endDirectory()


    def search(self):
        self.addDirectoryItem(32001, 'movieSearch', 'search.png', 'DefaultMovies.png')
        self.addDirectoryItem(32002, 'tvSearch', 'search.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32029, 'moviePerson', 'people-search.png', 'DefaultMovies.png')
        self.addDirectoryItem(32030, 'tvPerson', 'people-search.png', 'DefaultTVShows.png')

        self.endDirectory()

    def views(self):
        try:
            control.idle()

            items = [ (six.ensure_str(control.lang(32001)), 'movies'), (six.ensure_str(control.lang(32002)), 'tvshows'), (six.ensure_str(control.lang(32054)), 'seasons'), (six.ensure_str(control.lang(32038)), 'episodes') ]

            select = control.selectDialog([i[0] for i in items], six.ensure_str(control.lang(32049)))

            if select == -1: return

            content = items[select][1]

            title = six.ensure_str(control.lang(32059))
            url = '%s?action=addView&content=%s' % (sys.argv[0], content)

            poster, banner, fanart = control.addonPoster(), control.addonBanner(), control.addonFanart()

            item = control.item(label=title)
            item.setInfo(type='Video', infoLabels = {'title': title})
            item.setArt({'icon': poster, 'thumb': poster, 'poster': poster, 'banner': banner})
            item.setProperty('Fanart_Image', fanart)

            control.addItem(handle=int(sys.argv[1]), url=url, listitem=item, isFolder=False)
            control.content(int(sys.argv[1]), content)
            control.directory(int(sys.argv[1]), cacheToDisc=True)

            from resources.lib.modules import views
            views.setView(content, {})
        except:
            return


    def accountCheck(self):
        if traktCredentials == False and imdbCredentials == False:
            control.idle()
            control.infoDialog(six.ensure_str(control.lang(32042)), sound=True, icon='WARNING')
            sys.exit()


    def infoCheck(self, version):
        try:
            control.infoDialog('', six.ensure_str(control.lang(32074)), time=5000, sound=False)
            return '1'
        except:
            return '1'


    def clearCache(self):
        #control.idle()
        yes = control.yesnoDialog(control.lang(32056))
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear()
        control.infoDialog(six.ensure_str(control.lang(32057)), sound=True, icon='INFO')

    def clearCacheMeta(self):
        #control.idle()
        yes = control.yesnoDialog(control.lang(32056))
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear_meta()
        control.infoDialog(six.ensure_str(control.lang(32057)), sound=True, icon='INFO')

    def clearCacheProviders(self):
        #control.idle()
#        yes = control.yesnoDialog(control.lang(32056))
#        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear_providers()
        control.infoDialog(six.ensure_str(control.lang(32057)), sound=True, icon='INFO')

    def clearCacheSearch(self):
        #control.idle()
        yes = control.yesnoDialog(control.lang(32056))
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear_search()
        control.infoDialog(six.ensure_str(control.lang(32057)), sound=True, icon='INFO')

    def clearDebridCheck(self):
        #control.idle()
        yes = control.yesnoDialog(control.lang(32056))
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear_debrid()
        control.infoDialog(six.ensure_str(control.lang(32057)), sound=True, icon='INFO')

    def clearCacheAll(self):
        #control.idle()
        yes = control.yesnoDialog(control.lang(32056))
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear_all()
        control.infoDialog(six.ensure_str(control.lang(32057)), sound=True, icon='INFO')

    def addDirectoryItem(self, name, query, thumb, icon, context=None, queue=False, isAction=True, isFolder=True):
        try: name = six.ensure_str(control.lang(name))
        except: pass
        url = '%s?action=%s' % (sysaddon, query) if isAction == True else query
        thumb = os.path.join(artPath, thumb) if not artPath == None else icon
        cm = []
        if queue == True: cm.append((queueMenu, 'RunPlugin(%s?action=queueItem)' % sysaddon))
        if not context == None: cm.append((six.ensure_str(control.lang(context[0])), 'RunPlugin(%s?action=%s)' % (sysaddon, context[1])))
        item = control.item(label=name)
        item.addContextMenuItems(cm)
        item.setArt({'icon': thumb, 'thumb': thumb})
        if not addonFanart == None: item.setProperty('Fanart_Image', addonFanart)
        control.addItem(handle=syshandle, url=url, listitem=item, isFolder=isFolder)

    def endDirectory(self, cache=True):
        control.content(syshandle, 'addons')
        control.directory(syshandle, cacheToDisc=cache)
