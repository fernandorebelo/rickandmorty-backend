# Rick and Morty backend API

This is a backend API who returns all characters from the Rick and Morty show.

You can also get a specific character.

It gets the characters with a pagination of 20.

You can specify also a page.

This API has a Swagger documentation.

## Installation

Clone the project in your machine:

```bash
  $ git clone https://github.com/fernandorebelo/rickandmorty-backend
  $ cd rickandmorty-backend
```

Create a new virtual environment:

```bash
  $ py -3 -m venv .venv
  $ .venv\Scripts\activate
```

Install the requirements

```bash
  $ pip install -r requirements.txt
  cd my-project
```

Run the project:

```bash
  $ flask run --debug
```

Use your browser to access the swagger documentation:

```bash
  http:localhost/apidocs/
```

## API Reference

#### Get all items

```http
  GET /character
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item by name

```http
  GET /character?name=<character-name>
```

| Parameter | Type     | Description                          |
| :-------- | :------- | :----------------------------------- |
| `name`    | `string` | The name should be empty or any word |

#### Get item by name and page

```http
  GET /character?name=<character-name>&page=<page-number>
```

| Parameter | Type     | Description |
| :-------- | :------- | :---------- |
| `number`  | `string` |             |
