:- include("watch").
:- include("movies").

menu:-
	shell(clear),
	nl, write("==== Main Menu ====="), nl,
	write("=> 1. List ") , nl,
	write("=> 2. Add "), nl,
	write("=> 3. Remove "), nl,  
	write("=> 4. Sugession "), nl,
	write("=> 5. Save and Exit"), nl,
	read(X), 
	choice(X).

choice(1):-
	shell(clear),
	nl, write("++++++ WATCH LIST +++++++"), nl, 
	write("----------------------------"), nl,
	watchlist(X),
	format(' => ~s', [X]), nl,
	fail;true,
	get_char(X),nl,
	write("Press Enter To go back..."),
	get_char(X),
	menu.


choice(2):-
	shell(clear),
	write("Add a movie to watchlist: "),
	read(NewMovie),
	(	watchlist(NewMovie)
	->	write("==> The Movie is already on your Watchlist !!")
	;	format("~n The Movie is added to knowledge. "),
		assertz( watchlist(NewMovie) )
	),
	get_char(X),nl,
	write("Press Enter To go back..."),
	get_char(X),
	menu.

choice(3):- 
	shell(clear),
	nl, write("++++++ WATCH LIST +++++++"), nl, 
	write("----------------------------"), nl,
	watchlist(X),
	format(' => ~s', [X]), nl,
	fail;true,
	write("Remove {Type reset to delete all}: "),
	read(ToRemove),
	(	ToRemove = reset
	->	write("==> List is now empty..!!"),
		retractall(watchlist(_))
	;	write("Removed"), nl,
		retractall( watchlist(ToRemove) )
	),
	get_char(X),nl,
	write("Press Enter To go back..."),
	get_char(X),
	menu.


choice(4):-
	write("What Genre ? : "), 
	read(Cat),
	write("Minimum Rated : "),
	read(Rate),
	write("Do you want to search by Year? (yes/no): "),
	read(YearSearch),
	(  	YearSearch = yes
	->	write("Specify year: "), read(Year),
		movie(Movie, Rating, Year, Cat, _), Rating >= Rate,
		\+ watchlist(Movie),
		nl, write("Search Result ..."),nl,
		format("Movie Title    ~30|    Rating   "),nl
	;	nl, write("Search Result ..."),nl,
		format("Movie Title   ~30|    Rating   "),nl,
		movie(Movie, Rating, Released, Cat, _), Rating >= Rate,
		\+ watchlist(Movie)
	),
	
	format(' => ~s  ~30|      ~d ~n', [Movie, Rating]), fail;true,
	get_char(X),nl,
	write("Press Enter To go to menu."),
	get_char(X),
	shell(clear),
	menu.

choice(5):- 
	write("***** Saving the knowledge base \\//..."),
	tell('watch.pl'),
	listing(watchlist),
	told,
	write("=> Done !! ").

