from ..... import KeycloakResourceWithIdentifier


class ClientsByIdDefaultClientScopesById(KeycloakResourceWithIdentifier):
    def get_url(self):
        return f"{self._get_parent_url()}/{self.identifier}"

    async def add(self):
        connection = await self._get_connection()
        await connection.put(self.get_url())

    async def delete(self):
        connection = await self._get_connection()
        await connection.delete(self.get_url())