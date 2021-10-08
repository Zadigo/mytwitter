class SerializerMixin:
    def save(self, request, **kwargs):
        """Implements a request parameter on the save
        method for the Serializer"""
        
        validated_data = {**self.validated_data, **kwargs}

        if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
        else:
            self.instance = self.create(request, validated_data)

        if self.instance is None:
            raise ValueError('Instance is was not created')

        return self.instance
