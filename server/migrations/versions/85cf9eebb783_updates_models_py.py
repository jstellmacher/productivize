"""updates models.py

Revision ID: 85cf9eebb783
Revises: 
Create Date: 2023-06-22 16:29:36.635739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85cf9eebb783'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('_password_hash', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('pages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_pages_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=100), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('page_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['page_id'], ['pages.id'], name=op.f('fk_blocks_page_id_pages')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bulleted_list_blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['blocks.id'], name=op.f('fk_bulleted_list_blocks_id_blocks')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('callout_blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['blocks.id'], name=op.f('fk_callout_blocks_id_blocks')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('code_blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['blocks.id'], name=op.f('fk_code_blocks_id_blocks')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('divider_blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['blocks.id'], name=op.f('fk_divider_blocks_id_blocks')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('heading_blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['blocks.id'], name=op.f('fk_heading_blocks_id_blocks')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('image_blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['blocks.id'], name=op.f('fk_image_blocks_id_blocks')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('numbered_list_blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['blocks.id'], name=op.f('fk_numbered_list_blocks_id_blocks')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('quote_blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['blocks.id'], name=op.f('fk_quote_blocks_id_blocks')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('text_blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['blocks.id'], name=op.f('fk_text_blocks_id_blocks')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('toggle_blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['blocks.id'], name=op.f('fk_toggle_blocks_id_blocks')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('video_blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['blocks.id'], name=op.f('fk_video_blocks_id_blocks')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('video_blocks')
    op.drop_table('toggle_blocks')
    op.drop_table('text_blocks')
    op.drop_table('quote_blocks')
    op.drop_table('numbered_list_blocks')
    op.drop_table('image_blocks')
    op.drop_table('heading_blocks')
    op.drop_table('divider_blocks')
    op.drop_table('code_blocks')
    op.drop_table('callout_blocks')
    op.drop_table('bulleted_list_blocks')
    op.drop_table('blocks')
    op.drop_table('pages')
    op.drop_table('users')
    # ### end Alembic commands ###
