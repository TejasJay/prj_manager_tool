
# Alembic Commands Cheat Sheet

## Setup & Initialization
```bash
# Initialize Alembic in your project
alembic init alembic

# Create initial migration (after models are created)
alembic revision --autogenerate -m "Initial migration"

# Mark current database state as migrated (if tables already exist)
alembic stamp head
```

## Creating Migrations
```bash
# Auto-generate migration from model changes
alembic revision --autogenerate -m "Description of changes"

# Create empty migration file (manual editing)
alembic revision -m "Description of changes"

# Create migration with specific revision ID
alembic revision --rev-id=<revision_id> -m "Description"
```

## Applying Migrations
```bash
# Apply all pending migrations (upgrade to latest)
alembic upgrade head

# Upgrade to specific revision
alembic upgrade <revision_id>

# Upgrade one step forward
alembic upgrade +1

# Upgrade multiple steps
alembic upgrade +2
```

## Rolling Back Migrations
```bash
# Rollback one migration
alembic downgrade -1

# Rollback to specific revision
alembic downgrade <revision_id>

# Rollback to base (remove all migrations)
alembic downgrade base

# Rollback multiple steps
alembic downgrade -2
```

## Checking Status
```bash
# Show current database revision
alembic current

# Show migration history
alembic history

# Show detailed history with verbose output
alembic history --verbose

# Show specific revision details
alembic history <revision_id>

# Show pending migrations (what will be applied)
alembic heads
```

## Editing Migrations
```bash
# Edit the most recent migration
# (Open the file in alembic/versions/ and edit manually)
# Then apply: alembic upgrade head
```

## Common Workflows

### Daily Development Workflow
```bash
# 1. Make changes to models (in app/models/)
# 2. Generate migration
alembic revision --autogenerate -m "Add new field to User model"

# 3. Review the generated migration file
# (Check alembic/versions/xxxxx_add_new_field_to_user_model.py)

# 4. Apply migration
alembic upgrade head
```

### Adding a New Model
```bash
# 1. Create model file (e.g., app/models/comment.py)
# 2. Import in app/models/__init__.py
# 3. Generate migration
alembic revision --autogenerate -m "Add Comment model"

# 4. Apply migration
alembic upgrade head
```

### Modifying Existing Model
```bash
# 1. Edit model file (e.g., add new column)
# 2. Generate migration
alembic revision --autogenerate -m "Add email_verified column to User"

# 3. Review and apply
alembic upgrade head
```

### Production Deployment
```bash
# On production server:
# 1. Pull latest code
# 2. Apply all pending migrations
alembic upgrade head

# 3. Verify current state
alembic current
```

## Troubleshooting

### Merge Conflicts (Multiple Heads)
```bash
# Show all heads
alembic heads

# Merge multiple heads into one
alembic merge -m "Merge branches" <revision1> <revision2>
```

### Check Migration SQL Without Applying
```bash
# Show SQL that would be executed
alembic upgrade head --sql

# Show SQL for specific revision
alembic upgrade <revision_id> --sql
```

### Reset Everything (⚠️ DANGER - Deletes all data)
```bash
# Rollback all migrations
alembic downgrade base

# Re-apply all migrations
alembic upgrade head
```

## Tips & Best Practices

1. **Always review auto-generated migrations** before applying
2. **Use descriptive migration messages** - helps track changes
3. **Test migrations on dev/staging** before production
4. **Never edit applied migrations** - create new ones instead
5. **Keep migrations small** - one logical change per migration
6. **Commit migration files** to version control
7. **Use `alembic upgrade head`** in deployment scripts

## Quick Reference

| Command | Description |
|---------|-------------|
| `alembic current` | Show current revision |
| `alembic history` | Show all migrations |
| `alembic upgrade head` | Apply all pending migrations |
| `alembic downgrade -1` | Rollback one migration |
| `alembic revision --autogenerate -m "msg"` | Create migration from model changes |
| `alembic heads` | Show latest migration(s) |


---

Replace the content of `cheetsheet.md` with the above. It includes:
- Setup commands
- Creating migrations
- Applying/rolling back
- Status checks
- Common workflows
- Troubleshooting
- Best practices

Your Alembic setup looks good. The initial migration is created and ready to use.