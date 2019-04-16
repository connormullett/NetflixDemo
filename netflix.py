
import show_repo as repo


while True:
    prompt_choice = input('1. Create show\n' \
                          '2. View all shows\n' \
                          '3. Search Show\n' \
                          '4. Delete Show\n' \
                          '5. Update Show\n' \
                          '6. Exit\n>> ')

    if prompt_choice == '1':
        title = input('enter title: ')
        genre = input('enter genre: ')
        rating = input('enter rating: ')
        rate = int(rating)

        repo.create(title, genre, rate)

    elif prompt_choice == '2':
        print(repo.get_all())

    elif prompt_choice == '3':
        show_to_search = input('enter show name to search: ')
        searched_show = repo.get_show_by_name(show_to_search)
        print(searched_show)

    elif prompt_choice == '4':
        show_to_delete = input('enter show name to delete: ')
        repo.delete(show_to_delete)

    elif prompt_choice == '5':
        show_to_update = input('enter show to update: ')

        new_title = input('enter new title: ')
        new_genre = input('enter new genre: ')
        new_rating = input('enter new rating: ')

        repo.update(show_to_update, new_title, new_genre, new_rating)

    elif prompt_choice == '6':
        exit()

    else:
        print('INVALID ANSWER')

