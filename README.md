# Rick and Morty backend API

This is a backend API who returns all characters from the Rick and Morty show.

You can also get a specific character.

It gets the characters with a pagination of 20.

You can specify also a page.

This API has a Swagger documentation.

## Database

For now you need to have a database created on Postgresql. You need to ensure to have this configurations:

```
Host : localhost
Port : 5432
Database: postgres
User : postgres
Password : root
```

If you would like to test on another database you can change the configurations in the src/constants/http_status_codes.py file.

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

## Responses

#### Code 200

```http
  {
  "characters": [
    {
      "id": 0,
      "image": "string",
      "name": "string",
      "species": "string",
      "status": "string"
    }
  ],
  "page": 0,
  "pages": 0,
  "success": true,
  "total": 0
}
```

#### Code 400

```
The request was invalid
```

#### Code 404

```
No characters were found matching the search criteria
```
