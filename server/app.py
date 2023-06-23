from flask import request, session, jsonify
from flask_restful import Resource
from config import app, api, db
from models import User, Page, Block, TextBlock, HeadingBlock, ImageBlock

class UserResource(Resource):
    def get(self):
        # Retrieve user information based on the session
        user_id = session.get('user_id')
        if user_id:
            user = User.query.get(user_id)
            if user:
                return user.to_dict(), 200

        return {'message': 'User not authenticated'}, 401

api.add_resource(UserResource, "/users")  # Update the route to "/users"

class LoginResource(Resource):
    def post(self):
        # Handle user login
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Validate and handle login logic
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            # Login successful
            session['user_id'] = user.id
            return user.to_dict(), 200
        else:
            # Login failed
            return {'message': 'Invalid username or password'}, 401


class LogoutResource(Resource):
    def post(self):
        session.clear()
        return {"message": "Logout successful! Have a great day!"}, 200


class SignUpResource(Resource):
    def post(self):
        # Sign up a new user
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        
        # Validate and handle user sign-up logic
        
        # Create a new user object
        new_user = User(username=username, email=email)
        new_user.password_hash = password
        
        # Save the user to the database
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        
        return new_user.to_dict(), 201


class PageResource(Resource):
    def get(self, page_id=None):
        if page_id is None:
            # Get all pages
            pages = Page.query.all()
            # Serialize and return the pages
            return {'pages': [page.serialize() for page in pages]}
        else:
            # Get a specific page
            page = Page.query.get(page_id)
            if page is None:
                return {'message': 'Page not found'}, 404
            # Serialize and return the page
            return page.serialize()

    def post(self):
        # Create a new page
        data = request.get_json()
        title = data.get('title')
        
        # Validate and handle page creation logic
        
        # Create a new page object
        new_page = Page(title=title, user_id=session['user_id'])
        
        # Save the page to the database
        db.session.add(new_page)
        db.session.commit()
        
        return {'message': 'Page created successfully', 'page_id': new_page.id}, 201

    def put(self, page_id):
        # Update an existing page
        data = request.get_json()
        title = data.get('title')

        # Validate and handle page update logic

        page = Page.query.get(page_id)
        if page is None:
            return {'message': 'Page not found'}, 404

        # Update the page
        page.title = title
        db.session.commit()

        return {'message': 'Page updated successfully'}, 200

    def delete(self, page_id):
        # Delete an existing page
        page = Page.query.get(page_id)
        if page is None:
            return {'message': 'Page not found'}, 404

        # Delete the page
        db.session.delete(page)
        db.session.commit()

        return {'message': 'Page deleted successfully'}, 200


class BlockResource(Resource):
    def post(self, page_id):
        # Create a new block within a page
        data = request.get_json()
        block_type = data.get('type')
        content = data.get('content')

        # Validate and handle block creation logic

        block = None
        if block_type == 'text':
            block = TextBlock(content=content)
        elif block_type == 'heading':
            block = HeadingBlock(content=content)
        elif block_type == 'image':
            block = ImageBlock(content=content)

        if block:
            page = Page.query.get(page_id)
            if page is None:
                return {'message': 'Page not found'}, 404

            page.blocks.append(block)
            db.session.commit()

            return {'message': 'Block created successfully', 'block_id': block.id}, 201
        else:
            return {'message': 'Invalid block type'}, 400

    def put(self, page_id, block_id):
        # Update an existing block
        data = request.get_json()
        content = data.get('content')

        # Validate and handle block update logic

        block = Block.query.filter_by(id=block_id, page_id=page_id).first()
        if block is None:
            return {'message': 'Block not found'}, 404

        # Update the block
        block.content = content
        db.session.commit()

        return {'message': 'Block updated successfully'}, 200

    def delete(self, page_id, block_id):
        # Delete an existing block
        block = Block.query.filter_by(id=block_id, page_id=page_id).first()
        if block is None:
            return {'message': 'Block not found'}, 404

        # Delete the block
        db.session.delete(block)
        db.session.commit()

        return {'message': 'Block deleted successfully'}, 200


# class UsernameResource(Resource):
#     def get(self):
#         user_id = request.args.get('user_id')
#         user = User.query.get(user_id)
        
#         if user:
#             return jsonify({'username': user.username})
#         else:
#             return jsonify({'error': 'User not found'})


# Add the resource routes
api.add_resource(LoginResource, "/users/login")  # Add "/users/login" endpoint
api.add_resource(LogoutResource, "/users/logout")  # Add "/users/logout" endpoint
api.add_resource(SignUpResource, "/signup")
api.add_resource(PageResource, "/pages", "/pages/<int:page_id>")
api.add_resource(BlockResource, "/pages/<int:page_id>/blocks")
# api.add_resource(UsernameResource, "/username")

if __name__ == "__main__":
    app.run(port=5555, debug=True)
