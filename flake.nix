{
  description = "A flake for Rapsberry Pi 4 fan controller";

  inputs.nixpkgs.url = github:NixOS/nixpkgs/nixos-22.11;

  outputs = { self, nixpkgs }: {

    Packages =
      with import nixpkgs { system = "x86_64-linux"; };
      stdenv.mkDerivation {
        name = "fan_service";
        src = self;

        installPhase = ''install -t $out/fan_controller.py'';
      };
   };
}