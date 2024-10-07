# Команди, які я використав, і чому я їх використав

## File contents
### 1. [First task on Git](#1-first-task-on-git-1) 
### 2. [Second task on Git](#2-second-task-on-git-1)
### 3. [Third task on Git](#3-third-task-on-git-1)

## 1. First task on Git

### git branch <назва гілки>
``` git branch ``` — використав, щоб створити нову гілку ``` Revert ``` на віддаленому репозиторії для тестування функції ```git revert```. 

### git branch -D <назва гілки>
``` git branch ``` — використав, щоб видалити гілку Revert локально.

>[!NOTE]
>
>Саме прапорець визначає спосіб видалення гілки:
>\
>``` -D ``` — примусово видаляє гілку, ігноруючи те, чи була вона злита з основною гілкою (main / master).
>\
>``` -d ``` — видаляє гілку лише, коли зміни в ній змерджені в основну гілку, інакше видасть помилку.

### git rebase <назва гілки, з якої отримуються зміни>
``` git rebase ``` — використав цю команду для того, щоб залити зміни з гілки ``` main ``` в гілку ``` Rebase ```. Перед цим в ``` main ``` я створив файл README.md, а в ``` Rebase ``` — файл Rebase-First.

### git cherry-pick <SHA коміту, в якому комітили потрібні нам файли>
``` git cherry-pick ``` — використав цю команду для того, щоб залити файли, які були в коміті іншої гілки, в поточну гілку. Перед цим запустив команду ``` git log ``` в гілці, в якій був коміт, для отримання SHA коміту.

### git revert <SHA коміту, який потрібно відмінити>
``` git revert ``` — використав цю команду, щоб відмінити попередній коміт. При цьому довелося прописати ``` git push ```, щоб на репозиторії з'явився коміт, який показує, що відмінялося.

### git reset --hard <SHA коміту, який потрібно відмінити>
``` git reset ``` — використав команду, щоб видалити останній коміт локально. 

>[!NOTE]
>
>``` git reset ``` має різні прапорці.
>Візьмемо до прикладу гілку ``` master ```, де є коміти ``` A - B - C ```.
>\
>``` hard ``` — буде змінена робоча директорія на таку, яка була до відміненого коміта, тобто всі незакомічені і незапушені файли і директорії будуть видалені. Також буде переміщений вказівник індексу в історії комітів. При такій відміні коміта C індекс комітів переміститься на B.
>
> ``` mixed ``` — робоча директорія ніяк не зміниться, але буде переміщений вказівник індексу в історії комітів. При такій відміні коміта C індекс комітів переміститься на B (схоже на ``` hard ```).
>
> ``` soft ``` — цей прапорець не змінить робочої директорії і індексів в історії комітів. Тобто якщо одразу після такої відміни прописати ``` git commit ```, то цей коміт буде ідентичним до коміта, який ми відмінили.

### Відмінності між останніми двома командами:
>[!IMPORTANT]
>
>Різниця між ``` git revert ``` та ``` git reset ``` в тому, що перша команда відміняє зміни, які вже були закомічені і запушені, а друга команда відміняє зміни, які ще не були запушені, але вже закомічені.

## 2. Second task on Git+

### git commit --amend 
``` git commit --amend ``` - використав цю команду для того, щоб змінити повідомлення в незапушеному коміті. 

>[!NOTE]
>
>Ця команда має кілька доволі корисних прапорців, які застосовуються в наступному форматі: ``` git commit --amend --<прапорець> ```
>
>Перелік прапорців:
>\
>``` --no-edit ``` - використовується для того, щоб не змінювати текст коміта. Зазвичай використовується після наступних прапорців. Вся конструкція виглядає ось так: ``` git commit --amend --<потрібний прапорець> --no-edit ```.
> 
>``` --date ``` - використовується для зміни дати коміта. Вся команда виглядає наступним чином: ``` git commit --amend --date="<нова дата>" ```.
>
>``` --author ``` - використовується для зміни автора коміта на будь-якого іншого користувача.
>
>``` --reuse-message ``` - використовується для того, щоб використати текст минулих комітів як текст для поточного коміта.
>
>``` --reset-author ``` - використовується, коли необхідно скинути автора поточного коміта і встановити автором поточного юзера.

### git reset <прапорець> <SHA коміта, або прапорець HEAD>

> [!NOTE]
>
>В минулому розділі не розглянув такий прапорець, як ``` HEAD ```. Він корисний, оскільки можна не дізнаватися SHA коміта, який необхідно видалити. Так, наприклад, видалення останнього незапушеного коміта з цим прапорцем буде виглядати так: ``` HEAD~1 ```. Якщо потрібно, можна видалити два коміти: ``` HEAD~2 ```. Цифра, яку ви зазначите поряд з ним, буде визначати кількість комітів, які необхідно видалити.
>\
>Також за допомогою цієї команди можна видаляти мердж гілок, оскільки мерджі теж залишають коміти.

>[!WARNING]
>
> При такому видаленні, якщо попередні коміти були запушені, то у вас виникне суперечність з ``` main / master ``` гілкою. Тому видаляти коміти за допомогою цієї команди потрібно дуже обережно.

### git reflog
``` git reflog ``` - команда дозволяє переглядати журнал всіх команд, які були використані на локальному репозиторії git. 

### git tag <SHA коміту, на який потрібно створити тег>
``` git tag ``` - команда дозволяє створювати теги на певні коміти. 

>[!NOTE]
>
>Має кілька прапорців:
>\
> ``` -a ``` - створює текст-анотацію до тегу, який може містити інформацію про дату / автора / тощо.
>
>``` -d ``` - дозволяє видаляти теги. 
>
>``` -l ``` - виводить в консоль список всіх тегів, які наразі наявні на локальному репозиторії.
>
>``` -f ``` - дозволяє перезаписати вже створений тег.

### Різниця між git fork, git branch та git clone

>[!IMPORTANT]
>
>``` git fork ``` - не є стандартною командою для Git і додається сторонніми сервісами, як от GitHub або GitLab. Функція команди наступна: вона створює повну копію репозиторії в обліковому записі користувача в GitHub або GitLab. 
>
>``` git branch ``` - створює нову гілку в поточному репозиторії, що дозволяє вести розробку певної функції без впливу на ``` main / master ``` гілку. 
>
>``` git clone ``` - клонує весь репозиторій з облікового запису користувача на локальний комп'ютер. 
>
>З тексту вище можна зрозуміти, що команди відрізняються своїм базовим функціонал, і використовуються в різних ситуаціях.

### Що таке Pull Request?

> [!NOTE]
>
>``` pull request ``` - це пропозиція внести зміни з гілки / коміта в ``` main / master ``` гілку. Таку пропозицію ще називають ``` merge request ```. Основна перевага ``` pull request ``` полягає в тому, що інші деви можуть переглянути код, який подано на ріквест, і в разі невідповідності стандартам кодингу або коли він призводить до порушення вже існуючого функціоналу проекту, то такий ріквест може бути відхилений.


### Різниця між git pull та git fetch

>[!IMPORTANT]
>
>``` git pull ``` і ``` git fetch ``` — дві команди, які завантажують зміни з віддаленого репозиторію. Проте ``` git pull ``` не лише завантажує ці зміни, він їх ще й інтегрує в поточну робочу директорію. В той час як ``` git fetch ``` лише завантажує зміни і НЕ інтегрує їх, тобто після нього потрібно буде використати ``` git merge ```, щоб інтегрувати зміни в директорію.

### git stash
``` git stash ``` — використав цю команду, щоб приховати певні зміни, які не були закомічені і запушені. Цю команду можна використовувати, коли ми хочемо закомітити лише певну частину змін.

### git stash pop
``` git stash pop ``` — ця команда повертає (показує) зміни, які були приховані попередньою командою. Тобто, коли ми закомітили все, що хотіли, і повертаємося до роботи, то всі приховані зміни ми показуємо за допомогою цієї команди.

## 3. Third task on Git

### Що таке Git Hooks? Як з ними працювати?

>[!NOTE]
>
>``` Git Hooks ``` — це сценарії, які запускаються Git під час певних подій у життєвому циклі. Це потужний інструмент, який дозволяє оптимізувати та автоматизувати процес розробки. Функціонал хуків дуже обширний, і завдяки ним можна виконувати наступне:
>* Перевіряти синтаксичні помилки в коді
>* Форматувати код для забезпечення єдиного стилю форматування
>* Запускати тести для перевірки коду на працездатність
>* Перевіряти текст коміта на відповідність правилам
>* Перевіряти якість коду та відповідність правилам стилізації (eslint (JavaScript) / stylelint (CSS))
>* Перевіряти залежності (npm (JavaScript) / bandit (Python))
>* Автоматично розгортати проект на сервері після отримання змін
>
>Для роботи з Git Hooks потрібно перейти в папку ``` .git/hooks/ ```, де слід створити звичайний текстовий файл з назвою, що відповідає назві хука (наприклад, ``` pre-commit ``` або ``` post-merge ```). Потім у цей файл потрібно додати код хука, який виконуватиме необхідні дії. Не забудьте надати доступ до цього файлу. Опис всіх хуків доступний за посиланням: ``` [Git Hooks Documentation](https://git-scm.com/docs/githooks) ```. 
