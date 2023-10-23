# db-connector
The goal of this project is to port over the database related items from the cli tools we've built. Our expectation is users should have the ability to utilize the `query` and `connect` commands from our cli tool. The goal here is to port over any dependant code from the cli tool including the database folder, its dependencies and functionality. 

For info on how to test the db-connector once you've migrated over the sql related items is using supabase.

1. Visit this link to setup a free supabase account, https://supabase.com/dashboard/sign-in?
2. You can find free datasets online on kaggle, https://www.kaggle.com/
3. Once you've setup supabase, import your data into the supabase database
4. After importing, navigate into supabase and find your db URI connection info
5. Begin testing the migrated code

### Setting up dev env
At this point you should've setup your virtual env

**Installation**

```
pip install -r requirements.txt
```

After installing system dependencies be sure to install pre-commit

```
pip install pre-commit

pre-commit install
```

**Contribution guidelines**

We use commit messages for automated generation of project changelog. For every pull request we request contributors to be compliant with the following commit message notation.

```
<type>: <summary>

<body>
```

Accepted <type> values:

- new = newly implemented user-facing features
- chg = changes in existing user-facing features
- fix = user-facing bugfixes
- oth = other changes which users should know about
- dev = any developer-facing changes, regardless of new/chg/fix status

Summary (The first line)
The first line should not be longer than 75 characters, the second line is always blank and other lines should be wrapped at 80 characters.
