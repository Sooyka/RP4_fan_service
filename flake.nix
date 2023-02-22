{
  description = "A flake for Rapsberry Pi 4 fan controller";

  inputs.nixpkgs.url = github:NixOS/nixpkgs/nixos-22.11;

  outputs = { self, nixpkgs }: {

    defaultPackage."aarch64-linux" =
      with import nixpkgs { system = "aarch64-linux"; };
      stdenv.mkDerivation {
        name = "fan_service";
        src = self;

        installPhase = ''install -t $out/bin fan_controller.py '';
      };
   };
}