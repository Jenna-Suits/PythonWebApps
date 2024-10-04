# Add a new record
Note.objects.create(title="My Note", author="Me", body="NONE")

# List all objects
Note.objects.all()

# List specific objects
Note.objects.filter(author='Me')

# Get object by Primary Key
n = Note.objects.get(pk="4")

# Get object by Title
n = Note.objects.get(title="My Note")

# Show the details
print(n.pk, n.title, n.author)

# Get object by Title
n = Note.objects.get(title="My Note")

# Modify a field
n.body = "New text to show"
n.save()

# Delete one object
n = Note.objects.get(pk="16")
n.delete()

# Delete multiple objects
n = Note.objects.filter(author="Me").delete()

def list_notes():
    for n in Note.objects.all():
        print(n.pk, n.title, n.author)

