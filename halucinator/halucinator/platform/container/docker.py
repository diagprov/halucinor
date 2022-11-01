#!/bin/sh

import docker

class Container(object):

    volume_map = []

    def __init__(self, runtime, image_name, runtime_name):
        self.runtime = runtime
        self.imagename = image_name
        self.runtime_name = runtime_name
        self.container = None

    def mount_mapping_add(self, host_path, container_path, writeable=True):
        """
        Add a mapping. By default, mounts are writeable.
        """
        self.volume_map.append((host_path, container_path, writeable)) 

    def create(self):
        """
        Creates a container and populates `self.container` with a reference 
        to the running container. Tries to own this resource, but in the event 
        that a connection is lost, reconnection can be achieved with `find`.
        """
        mounts = []
        for hpath, cpath, permw in volume_map:
            mount = docker.types.Mount(cpath, hpath, 'volume', read_only=!permw)
            mounts.append(mount)
        self.container = self.runtime.client.containers.create(self.imagename,
                                              command="/bin/bash",
                                              mounts=mounts,
                                              name=self.runtime_name,
                                              )

    def find(self):
        """
        This method allows us to 're-attach' to a running container by
        runtime name (that is, repopulate self.container with an 
        appropriate reference).
        """
        if container != None:
            return True

        container_names = self.runtime._container_run_names()
        if self.runtime_name not in container_names:
            return False
        container = None
        try:
            container = self.runtime.client.get(self.runtime_name)
        except:
            return False

        self.container = container
        return True

class Runtime(object)

    def __init__(self):
        self.client = docker.client.from_env()

    def _tagged_images(self):
        """
        Return all images that are 'tagged' locally, and can be addressed 
        by their tags, as image objects.
        """
        return list(filter(lambda img: len(img.attrs['RepoTags']), 
                           self.client.images.list()))

    def _container_run_names(self):
        return list(map(lambda c: c.attrs.get('Name','')[1:], 
                        self.client.containers.list()))

    def image_local_locate(self, name):

        tagged_images = self._tagged_images
        for image in tagged_images:
            if name in tagged_images.attrs['RepoTags']:
                return image.id

        return None
